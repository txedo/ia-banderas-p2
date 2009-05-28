#!/usr/bin/python
# -*- coding: utf-8 -*-

import Ice, sys, time, threading, psyco, datetime

Ice.loadSlice('-I/usr/share/slice ../slice/Practica.ice')

import Practica

from tablero import *
from equipo import *
from estado import *
from nodo import *
from minimax import *

psyco.full()


def Inicializar(mapa, equipos, tablero):
    global_vars.casillasIniciales = []
    global_vars.banderasObjetivo = []
    global_vars.distanciaBanderas = {}
    # Tiempo del turno
    global_vars.deadline = mapa.tiempo
    # ID de usuario, MIN y MAX
    global_vars.idUsuario = ((mapa.idUsuario - 1)%2)+1
    print "idUsuario %d" % (global_vars.idUsuario)
    global_vars.MAX = global_vars.idUsuario - 1
    print "MAX %d" % (global_vars.MAX)
    global_vars.MIN = (global_vars.MAX + 1)%2
    print "MIN %d" % (global_vars.MIN)
    # Filas y columnas del tablero
    global_vars.filasTablero = mapa.dimy
    global_vars.columnasTablero = mapa.dimx
    # Inicializamos las casillas iniciales que nos da el servidor
    for index,casilla in enumerate(mapa.casillas):
        cas = Casilla(index+1,casilla)
        global_vars.casillasIniciales.append(cas)
        if casilla == T_BANDERA:
            tablero.banderas += 1
            global_vars.banderasObjetivo.append(index+1)
    # Inicializamos las distancias a cada bandera
    for i in global_vars.banderasObjetivo:
        distancias = []
        distancias = tablero.WayTracking(i)
        global_vars.distanciaBanderas[i] = distancias[:]
    # Inicializamos los equipos. Cada equipo inicializa sus jugadores en el constructor
    idEquipo = 1
    for i in mapa.jugadores:
        if idEquipo == i.equipo:
            eqAux = Equipo (idEquipo, mapa.jugadores)
            equipos.append(eqAux)
            idEquipo += 1
    

class Client (Ice.Application):

    def printHelp(self):
        print "\nEjecucion del cliente para las practicas de IA: \n"
        print "- Para jugar una partida individual ejecutar dos instancias del programa con la linea: ./Client 1 --Ice.Config=(Ruta Archivo .config)\n"
        print "- Para jugar una competicion ejecutar una instancia del programa con la linea: ./Client 2 --Ice.Config=(Ruta Archivo .config)\n  Esperar a que el oponente se una a la partida.\n\n"

    def jugarPartida(self, dni, partida):
        jugando = True;
        mapa = partida.obtenerMapa(dni)
        time.sleep(2)
        equipos = []
        tablero = Tablero()
        Inicializar (mapa, equipos, tablero)
        estado_actual = Estado (tablero, equipos)
        nodo_actual = Nodo (estado_actual)
        minimax = Minimax(nodo_actual)
        #print mapa
        print "Tiempo de los turnos configurado en %d segundos." % (global_vars.deadline)
        print "Esperando a que se una otro jugador..."
        
        while jugando:
            moviendo = True
            infoJugada = partida.pedirTurno(mapa.idUsuario)

            print "Movimiento realizado por el oponente, resultado y token para realizar el movimiento:"
            print infoJugada
            # Esta condicion es para corregir desde el cliente un bug del servidor
            if infoJugada.mov.idJugador == -1 and infoJugada.mov.mov == -1:
                infoJugada.resultado = 0
            
            if infoJugada.resultado != 0:
                if infoJugada.resultado == 1:
                    print "Has GANADO!"
                    jugando = False
                    moviendo = False
                else:
                    print "Has PERDIDO!"
                    jugando = False
                    moviendo = False
                break

            while moviendo:
                if infoJugada.mov.idJugador <> -1 and infoJugada.mov.mov <> -1:
                    # Actualizamos el estado con los cambios que ha provocado en el tablero la accion del oponente
                    jug = (infoJugada.mov.idJugador-1)%(len(mapa.jugadores)/2)
                    casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MIN].jugadores[jug].casilla)
                    nodo_actual.estado.actualizarEstado(global_vars.MIN, jug, tablero.casillaActual(casillas[infoJugada.mov.mov-1]))
                    minimax.nodoMejor = copy.deepcopy(nodo_actual)
                    print str(estado_actual.equipos[global_vars.MIN])
                
                d1 = datetime.datetime.now()
                # Creamos un hilo que lanzara la busqueda minimax
                minimax.timeout = False
                buscador = threading.Thread(target=minimax.decision_minimax, args=())
                buscador.start()
                # Ejecutamos la funcion durmiente que indicara cuando parar la busqueda
                minimax.Sync()
                
                (jugador, movimiento) = minimax.nodoMejor.accion
                print datetime.datetime.now()-d1            
                if jugador == 0:
                    break

                try:
                    # Mandamos el movimiento al servidor
                    devuelto = partida.jugada(mapa.idUsuario, jugador, movimiento, infoJugada.token)
                    print "Movimiento realizado: " + str(devuelto)
                    print "Jugador %d\nAccion %d" % (jugador,movimiento)
                    moviendo = False;
                    # Actualizamos el estado con los cambios que ha provocado nuestro movimiento
                    jug = (jugador-1)%(len(mapa.jugadores)/2)
                    casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MAX].jugadores[jug].casilla)
                    nodo_actual.estado.actualizarEstado(global_vars.MAX, jug, tablero.casillaActual(casillas[movimiento-1]))
                    minimax.nodoMejor = copy.deepcopy(nodo_actual)
                    print str(estado_actual.equipos[global_vars.MAX])
                    
                except Practica.TokenIncorrectoError, e:
                    print e.reason
                    print "El temporizador ha expirado. Has PERDIDO la partida."
                    jugando = False
                    moviendo = False

                except Practica.MovimientoIncorrectoError, e:
                    print e.reason
                    print "Ha introducido un movimiento no valido. Introduzca de nuevo el movimiento."

    def run(self, argv):
        dni = "71219116"
        password = "asdfqwer"

        if len(argv) == 1 or len(argv) > 2:
            self.printHelp()

        else:
            base = self.communicator().stringToProxy("AutenticacionObject")
            autenticacion = Practica.AutenticacionPrx.checkedCast(base)
            partida = None
            if not autenticacion:
                print "ERROR"

            try:
                partida = autenticacion.login(dni, password)
                print str(partida)

            except Practica.PasswordIncorrectaError, e:
                print e.reason
            except Practica.UsuarioIncorrectoError, e:
                print e.reason
            except Practica.NoExisteContrincanteError, e:
                print e.reason
            except Practica.NoExistePartidaError, e:
                print e.reason

            if argv[1] == "1" and partida != None:
                self.jugarPartida(dni, partida)
                try:
                    autenticacion.finalizarPartida(dni, password)
                except Practica.UnknownException:
                    pass
                    
            elif argv[1] == "2" and partida != None:
                self.jugarPartida(dni, partida)
                print "RECUPERANDO SEGUNDA PARTIDA"
                time.sleep(5)
                self.jugarPartida(dni, partida)
                try:
                    autenticacion.finalizarPartida(dni, password)
                except Practica.UnknownException:
                    pass
        
            elif partida != None:
                print "ERROR: El argumento introducido no es correcto\n"
                self.printHelp()
        
Client().main(sys.argv)
