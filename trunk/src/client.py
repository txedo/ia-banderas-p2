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
    # ID de usuario, MIN y MAX
    global_vars.idUsuario = ((mapa.idUsuario - 1)%2)+1
    #print "idUsuario %d" % (global_vars.idUsuario)                                      #test
    global_vars.MAX = global_vars.idUsuario - 1
    #print "MAX %d" % (global_vars.MAX)                                                  #test
    global_vars.MIN = (global_vars.MAX + 1)%2
    #print "MIN %d" % (global_vars.MIN)                                                  #test
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

    def run(self, argv):
        base = self.communicator().stringToProxy("AutenticacionObject")

        autenticacion = Practica.AutenticacionPrx.checkedCast(base)
        if not autenticacion:
            print "ERROR"

        global_vars.deadline = input ("Introduce la duracion de cada turno: ")

        partida = autenticacion.login("71219116", "asdfqwer")
        print str(partida)

        mapa = partida.obtenerMapa("71219116")
        equipos = []
        tablero = Tablero()
        Inicializar (mapa, equipos, tablero)
        estado_actual = Estado (tablero, equipos)
        nodo_actual = Nodo (estado_actual)
        minimax = Minimax(nodo_actual)
        #print mapa
        print "Esperando a que se una otro jugador..."
        
        while True:
            infoJugada = partida.pedirTurno(global_vars.idUsuario)
            print infoJugada
            if infoJugada.resultado != 0:
                if infoJugada.resultado == 1:
                    print "Has ganado. Juguemos la siguiente partida"
                else:
                    print "Has perdido. Juguemos la siguiente partida"
                break
                
            if infoJugada.mov.idJugador <> -1 and infoJugada.mov.mov <> -1:
                jug = (infoJugada.mov.idJugador-1)%(len(mapa.jugadores)/2)
                casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MIN].jugadores[jug].casilla)
                estado_actual.actualizarEstado(global_vars.MIN, jug, tablero.casillaActual(casillas[infoJugada.mov.mov-1]))
                minimax.nodoMejor = copy.deepcopy(nodo_actual)
                print str(estado_actual.equipos[global_vars.MIN])
            
            d1 = datetime.datetime.now()
            bella_durmiente = threading.Thread(target=minimax.Sync, args=())
            buscador = threading.Thread(target=minimax.decision_minimax, args=())
            bella_durmiente.start()
            buscador.start()
            bella_durmiente.join()
            #minimax.Sync()
            
            (jugador, movimiento) = minimax.nodoMejor.accion
            print datetime.datetime.now()-d1            
            #jugador = int(raw_input("Jugador: "))
            if jugador == 0:
                break
            #movimiento = int(raw_input("Movimiento: "))
            try:
                print "idJugador = ", jugador
                print "mov = ", movimiento
                devuelto = partida.jugada(global_vars.idUsuario, jugador, movimiento, infoJugada.token)
                print "Movimiento realizado: " + str(devuelto)
            except Practica.MovimientoIncorrectoError, e:
                print e.reason
                print "Has hecho un movimiento incorrecto. Durmiendo %d segundos para perder automaticamente" % (global_vars.deadline)
                time.sleep(global_vars.deadline)
                break
            except Practica.TokenIncorrectoError, e:
                print e.reason
                print "Has agotado el tiempo. Juguemos la siguiente partida"
                break
            
            jug = (jugador-1)%(len(mapa.jugadores)/2)
            casillas = estado_actual.tablero.idCasillasVecinas(equipos[global_vars.MAX].jugadores[jug].casilla)
            estado_actual.actualizarEstado(global_vars.MAX, jug, tablero.casillaActual(casillas[movimiento-1]))
            minimax.nodoMejor = copy.deepcopy(nodo_actual)
            print str(estado_actual.equipos[global_vars.MAX])
        
        
        raw_input("Presione ENTER para continuar...")

        mapa = partida.obtenerMapa("71219116")
        equipos = []
        tablero = Tablero()
        Inicializar (mapa, equipos, tablero)
        estado_actual = Estado (tablero, equipos)
        nodo_actual = Nodo (estado_actual)
        minimax = Minimax(nodo_actual)
        #print mapa
        
        while True:
            #infoJugada = partida.pedirTurno(mapa.idUsuario)
            infoJugada = partida.pedirTurno(global_vars.idUsuario)
            print infoJugada
            if infoJugada.resultado != 0:
                if infoJugada.resultado == 1:
                    print "Has ganado"
                else:
                    print "Has perdido"
                break

            jugador = int(raw_input("Jugador: "))
            if jugador == 0:
                break
            movimiento = int(raw_input("Movimiento: "))
            try:
                #devuelto = partida.jugada(mapa.idUsuario, jugador, movimiento, infoJugada.token)
                devuelto = partida.jugada(global_vars.idUsuario, jugador, movimiento, infoJugada.token)
                print "Movimiento realizado: " + str(devuelto)
            except Practica.MovimientoIncorrectoError, e:
                print e.reason
                print "Has hecho un movimiento incorrecto. Durmiendo %d segundos para perder automaticamente." % (global_vars.deadline)
                time.sleep(global_vars.deadline)
                break
            except Practica.TokenIncorrectoError, e:
                print e.reason
                print "Has agotado el tiempo y has perdido la partida."
                break
        
        print "Han finalizado las dos partidas"
        time.sleep(3)
        ret = autenticacion.finalizarPartida("71219116","asdfqwer")

Client().main(sys.argv)
