#!/usr/bin/python
# -*- coding: utf-8 -*-

import Ice, sys, time

Ice.loadSlice('-I/usr/share/slice ../slice/Practica.ice')

import Practica

class Client (Ice.Application):

    def run(self, argv):
        
        base = self.communicator().stringToProxy("AutenticacionObject")

        autenticacion = Practica.AutenticacionPrx.checkedCast(base)
        if not autenticacion:
            print "ERROR"

        partida = autenticacion.login("71219116", "asdfqwer")

        print str(partida)

        tablero = partida.obtenerMapa("71219116")
        print tablero
        
        while True:
            infoJugada = partida.pedirTurno(tablero.idUsuario)
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
            devuelto = partida.jugada(tablero.idUsuario, jugador, movimiento, infoJugada.token)
            print "Movimiento realizado: " + str(devuelto)

        val = int(raw_input("Introduzca un valor entero para continuar "))

        tablero = partida.obtenerMapa("71219116")
        print tablero
        
        while True:
            infoJugada = partida.pedirTurno(tablero.idUsuario)
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
            devuelto = partida.jugada(tablero.idUsuario, jugador, movimiento, infoJugada.token)
            print "Movimiento realizado: " + str(devuelto)
        
        print "Han finalizado las dos partidas"
        time.sleep(3)
#        ret = autenticacion.finalizarPartida("71219116","asdfqwer")

Client().main(sys.argv)
