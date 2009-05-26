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
    #global_vars.deadline = 6
    # ID de usuario, MIN y MAX
    global_vars.idUsuario = ((mapa.idUsuario - 1)%2)+1
    print "idUsuario %d" % (global_vars.idUsuario)                                      #test
    global_vars.MAX = global_vars.idUsuario - 1
    print "MAX %d" % (global_vars.MAX)                                                  #test
    global_vars.MIN = (global_vars.MAX + 1)%2
    print "MIN %d" % (global_vars.MIN)                                                  #test
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
    # TEST PARA VER SI SE INICIALIZAN BIEN LAS CASILLASINICIALES                       #test
    #print mapa.casillas                                                                #test
    #cad = "["                                                                          #test
    #for i in global_vars.casillasIniciales: cad += str(i.tipo) + ", "                  #test
    #cad += "]"                                                                         #test
    #print cad                                                                          #test
    # Inicializamos las distancias a cada bandera
    for i in global_vars.banderasObjetivo:
        distancias = []
        distancias = tablero.WayTracking(i)
        global_vars.distanciaBanderas[i] = distancias[:]
    # TEST PARA VER SI SE CALCULAN BIEN LAS DISTANCIAS                                  #test
    #for j in global_vars.distanciaBanderas:                                             #test
    #    f=0                                                                             #test
    #    for i in range(global_vars.filasTablero):                                       #test
    #        print global_vars.distanciaBanderas[j][f:(i+1)*global_vars.columnasTablero] #test
    #        f += global_vars.columnasTablero                                            #test
    # Inicializamos los equipos. Cada equipo inicializa sus jugadores en el constructor
    idEquipo = 1
    for i in mapa.jugadores:
        if idEquipo == i.equipo:
            eqAux = Equipo (idEquipo, mapa.jugadores)
            equipos.append(eqAux)
            idEquipo += 1
    # TEST PARA VER SI SE INICIALIZAN BIEN LOS EQUIPOS Y LOS JUGADORES                  #test
    #for i in equipos: print str(i)                                                      #test
    

class Client (Ice.Application):

    def printHelp(self):
        print "\nEjecucion del cliente para las practicas de IA: \n"
        print "- Para jugar una partida individual ejecutar dos instancias del programa con la linea: ./Client 1 --Ice.Config=(Ruta Archivo .config)\n"
        print "- Para jugar una competición ejecutar una instancia del programa con la linea: ./Client 2 --Ice.Config=(Ruta Archivo .config)\n  Esperar a que el oponente se una a la partida.\n\n"

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
            if infoJugada.mov.idJugador == -1 and infoJugada.mov.mov == -1: infoJugada.resultado = 0 # Apaño basto
            if infoJugada.resultado != 0:
                if infoJugada.resultado == 1:
                    print "¡Has GANADO!"
                    jugando = False
                    moviendo = False
                else:
                    print "¡Has PERDIDO!"
                    jugando = False
                    moviendo = False
                break

            while moviendo:
                #
                #INTRODUCE EL CODIGO PARA CALCULAR LOS MOVIMIENTOS AQUI
                #TEN EN CUENTA EL TIEMPO ESTABLECIDO PARA CALCULAR UN MOVIMIENTO
                #
                #En jugador debes indicar que jugador deseas mover.
                #En movimiento debes indicar que movimiento deseas realizar [ 1 | 2 | 3 | 4 | 5 | 6 ]
                #
                #Si introduces un movimiento incorrecto podrás realizar otro, pero el temporizador no se reiniciara
                #

                #Introducir los movimientos manualmente
                #jugador = int(raw_input("Jugador: "))
                #movimiento = int(raw_input("Movimiento: "))
                if infoJugada.mov.idJugador <> -1 and infoJugada.mov.mov <> -1:
                    jug = (infoJugada.mov.idJugador-1)%(len(mapa.jugadores)/2)
                    casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MIN].jugadores[jug].casilla)
                    nodo_actual.estado.actualizarEstado(global_vars.MIN, jug, tablero.casillaActual(casillas[infoJugada.mov.mov-1]))
                    print "el otro me ha dejado %d banderas" % (nodo_actual.estado.tablero.banderas)
                    #print "--------> prof del nodo_actual: ", nodo_actual.profundidad
                    minimax.nodoMejor = copy.deepcopy(nodo_actual)
                    print str(estado_actual.equipos[global_vars.MIN])
                    for i in tablero.casillasModificadas: print i.idCasilla
                
                #print "ANTES"
                #print "band ", estado_actual.tablero.banderas
                #estado_actual.minimaDistancia(global_vars.MAX, 1)
                #estado_actual.minimaDistancia(global_vars.MIN, 1)
                #raw_input()
                
                d1 = datetime.datetime.now()
                #bella_durmiente = threading.Thread(target=minimax.Sync, args=())
                buscador = threading.Thread(target=minimax.decision_minimax, args=())
                #bella_durmiente.start()
                buscador.start()
                #bella_durmiente.join()
                minimax.Sync()
                
                (jugador, movimiento) = minimax.nodoMejor.accion
                #print "supuesto nodo mejor. Prof: ", minimax.nodoMejor.profundidad
                #print "utilidad de nodoMejor: ", minimax.nodoMejor.utilidad
                (jugador, movimiento) = minimax.nodoMejor.accion
                print datetime.datetime.now()-d1            
                #jugador = int(raw_input("Jugador: "))
                if jugador == 0:
                    break
                #movimiento = int(raw_input("Movimiento: "))

                try:
                    print "-------------------->" , minimax.nodoMejor.profundidad
                    devuelto = partida.jugada(mapa.idUsuario, jugador, movimiento, infoJugada.token)
                    print "Movimiento realizado: " + str(devuelto)
                    moviendo = False;
                    jug = (jugador-1)%(len(mapa.jugadores)/2)
                    casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MAX].jugadores[jug].casilla)
                    nodo_actual.estado.actualizarEstado(global_vars.MAX, jug, tablero.casillaActual(casillas[movimiento-1]))
                    #print "DESPUES"
                    #print "band ", estado_actual.tablero.banderas
                    #estado_actual.minimaDistancia(global_vars.MAX, [], 1)
                    #estado_actual.minimaDistancia(global_vars.MIN, [], 1)
                    minimax.nodoMejor = copy.deepcopy(nodo_actual)
                    print str(estado_actual.equipos[global_vars.MAX])
                    for i in tablero.casillasModificadas: print i.idCasilla
                    
                except Practica.TokenIncorrectoError, e:
                    print e.reason
                    print "El temporizador ha expirado. Has PERDIDO la partida."
                    jugando = False
                    moviendo = False

                except Practica.MovimientoIncorrectoError, e:
                    print e.reason
                    print "Ha introducido un movimiento no válido. Introduzca de nuevo el movimiento."

    def run(self, argv):
        #INTRODUCE TU DNI Y TU PASSWORD AQUI
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
