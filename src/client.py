#!/usr/bin/python
# -*- coding: utf-8 -*-

import psyco

import Ice, sys, time

Ice.loadSlice('-I/usr/share/slice ../slice/Practica.ice')

import Practica


from tablero import *
from equipo import *


def Inicializar(mapa, equipos, tablero):
    # ID de usuario, MIN y MAX
    global_vars.idUsuario = mapa.idUsuario
    if mapa.idUsuario == 1 or mapa.idUsuario == 3:
        global_vars.MAX = 0
        global_vars.MIN = 1
    elif mapa.idUsuario == 2 or mapa.idUsuario == 4:
        global_vars.MAX = 1
        global_vars.MIN = 0
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
    # Inicializamos los equipos. Cada equipo inicializa sus jugadores en el constructor
    idEquipo = 1
    for i in mapa.jugadores:
        if idEquipo == i.equipo:
            eqAux = Equipo (idEquipo, mapa.jugadores)
            equipos.append(eqAux)
            idEquipo += 1


class Client (Ice.Application):

    def run(self, argv):
        
        psyco.full()
        base = self.communicator().stringToProxy("AutenticacionObject")

        autenticacion = Practica.AutenticacionPrx.checkedCast(base)
        if not autenticacion:
            print "ERROR"

        partida = autenticacion.login("71219116", "asdfqwer")
        print str(partida)

        mapa = partida.obtenerMapa("71219116")
        equipos = []
        tablero = Tablero()
        Inicializar (mapa, equipos, tablero)
        #print mapa
        #for i in equipos: print str(i)
        #print mapa.casillas
        #cad = "["
        #for i in global_vars.casillasIniciales: cad += str(i.tipo) + ", "
        #cad += "]"
        #print cad
        print "Esperando a que se una otro jugador..."
        
        while True:
            infoJugada = partida.pedirTurno(mapa.idUsuario)
            print infoJugada
            if infoJugada.resultado != 0:
                if infoJugada.resultado == 1:
                    print "Has ganado. Juguemos la siguiente partida"
                else:
                    print "Has perdido. Juguemos la siguiente partida"
                break

            jugador = int(raw_input("Jugador: "))
            if jugador == 0:
                break
            movimiento = int(raw_input("Movimiento: "))
            devuelto = partida.jugada(mapa.idUsuario, jugador, movimiento, infoJugada.token)
            print "Movimiento realizado: " + str(devuelto)

        raw_input("Presione ENTER para continuar...")

        mapa = partida.obtenerMapa("71219116")
        equipos = []
        tablero = Tablero()
        Inicializar (mapa, equipos, tablero)
        print mapa
        
        while True:
            infoJugada = partida.pedirTurno(mapa.idUsuario)
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
            devuelto = partida.jugada(mapa.idUsuario, jugador, movimiento, infoJugada.token)
            print "Movimiento realizado: " + str(devuelto)
        
        print "Han finalizado las dos partidas"
        time.sleep(3)
        #ret = autenticacion.finalizarPartida("71219116","asdfqwer")

Client().main(sys.argv)
