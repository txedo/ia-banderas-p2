from jugador import *


class Equipo:
    def __init__ (self, idEquipo, jugadores_ice, banderasCapturadas = 0):
        self.idEquipo = idEquipo
        self.banderasCapturadas = banderasCapturadas
        self.numeroJugadores = len(jugadores_ice)
        self.jugadores = []
        for i,j in enumerate(jugadores_ice):
            #jugadores_ice es una estructura de tipo Jugador definida en Practica.ice
            jug = Jugador(i+1, self.idEquipo, j.casilla, j.energia)
            self.jugadores.append(jug)
            
            
    def getIdEquipo (self):
        return self.idEquipo
        
        
    def getBanderasCapturadas (self):
        return self.banderasCapturadas
        
       
    def setBanderasCapturadas (self, valor):
        self.banderasCapturadas = valor
        
        
    def capturarBandera(self):
        self.setBanderasCapturadas(self.getBanderasCapturadas() + 1)
        
        
    def getNumeroJugadores(self):
        return self.numeroJugadores
        
        
    def getJugadores(self):
        return self.jugadores
    
    
    def __str__ (self):
        cadena = "EQUIPO::: ID Equipo: %d\n" % self.getIdEquipo()
        cadena += "EQUIPO::: Banderas capturadas: %d\n" % self.getBanderasCapturadas()
        cadena += "EQUIPO::: Numero de jugadores: %d\n" % self.getNumeroJugadores()
        for i in self.jugadores: cadena += str(i)
        return cadena

