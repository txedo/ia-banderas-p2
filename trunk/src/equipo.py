from jugador import *
import psyco

psyco.full()


class Equipo:
    def __init__ (self, idEquipo, jugadores_ice, banderasCapturadas = 0):
        self.idEquipo = idEquipo
        self.banderasCapturadas = banderasCapturadas
        self.jugadores = []
        for jug in jugadores_ice:
            #jugadores_ice es una estructura de tipo Jugador definida en Practica.ice
            if jug.equipo == self.idEquipo:
                jugAux = Jugador(jug.idJugador, jug.equipo, jug.casilla, jug.energia)
                self.jugadores.append(jugAux)
            
            
    def getIdEquipo (self):
        return self.idEquipo
        
        
    def getBanderasCapturadas (self):
        return self.banderasCapturadas
        
       
    def setBanderasCapturadas (self, valor):
        self.banderasCapturadas = valor
        
        
    def capturarBandera(self):
        self.setBanderasCapturadas(self.getBanderasCapturadas() + 1)
        
        
    def getJugadores(self):
        return self.jugadores
        
        
    def getEnergiaTotal(self):
        energiaTotal = 0
        for i in self.jugadores:
            energiaTotal += i.energia
        return energiaTotal
    
    
    def __str__ (self):
        cadena = "EQUIPO::: ID Equipo: %d\n" % self.getIdEquipo()
        cadena += "EQUIPO::: Banderas capturadas: %d\n" % self.getBanderasCapturadas()
        for i in self.jugadores: cadena += str(i)
        return cadena

