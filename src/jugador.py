import global_vars, config
import psyco

psyco.full()

class Jugador:
    def __init__ (self, idJugador, equipo, casilla, energia, hacha = 0, barca = 0, pala = 0, banderas = 0, zumo = 0):
        self.idJugador = idJugador
        self.equipo = equipo
        self.casilla = casilla # Identificador (int) de la casilla actual del jugador
        self.energia = energia
        self.hacha = hacha
        self.barca = barca
        self.pala = pala

        
    def getIdJugador (self):
        return self.idJugador
        
        
    def getEquipo (self):
        return self.equipo
        
        
    def getCasilla (self):
        return self.casilla
        
        
    def setCasilla (self, valor):
        self.casilla = valor
        
        
    def getEnergia (self):
        return self.energia
        
        
    def setEnergia (self, valor):
        self.energia = valor
        
    
    def beberZumo (self):
        self.energia = self.energia + 20
        
        
    def perderEnergia (self, valor):
        energiaActual = self.energia - valor
        if energiaActual > 0:
            self.energia = energiaActual
            return True
        else:
            return False
        
        
    def getHacha (self):
        return self.hacha
        
        
    def setHacha (self, valor):
        self.hacha = valor
        
        
    def usarHacha (self):
        """ Cuando se entra en una casilla de bosque se utiliza el hacha siempre
        que se tenga. No hay eleccion a utilizarla o no.
            DEVUELVE True si ha utilizado el hacha y False si no la ha utilizado
        """
        if self.getHacha() > 0:
            if self.perderEnergia(4):
                self.setHacha(self.getHacha() - 1)
                return (True, True) # Se mueve y usa el hacha
            else:
                return (False, False) # No se puede mover asi que no usa el hacha
        else:
            if self.perderEnergia(8):
                return (True, False) # Se mueve y no usa el hacha
            else:
                return (False, False) # No se puede mover y no tiene hacha
    
    
    def cogerHacha (self):
        self.setHacha(self.getHacha() + 20)
        
        
    def getBarca (self):
        return self.barca
        
        
    def setBarca (self, valor):
        self.barca = valor
    
    
    def usarBarca (self):
        """ Cuando se entra en una casilla de agua se utiliza la barca siempre
        que se tenga. No hay eleccion a utilizarla o no.
        """
        if self.getBarca() > 0:
            self.perderEnergia(3)
            self.setBarca(self.getBarca() - 1)
        else:
            self.perderEnergia(6)
            
    
    def cogerBarca (self):
        self.setBarca(self.getBarca() + 20)
        
        
    def getPala (self):
        return self.pala
        
        
    def setPala (self, valor):
        self.pala = valor
        
        
    def usarPala (self):
        if self.getPala() > 0:
            self.setPala(self.getPala() - 2)
            return True
        else:
            return False
    
    
    def cogerPala (self):
        self.setPala(self.getPala() + 10)
        
        
    def __str__ (self):
        cadena = "JUGADOR::: ID Jugador: %d\n" % self.getIdJugador()
        cadena += "JUGADOR::: Equipo: %d\n" % self.getEquipo()
        cadena += "JUGADOR::: Casilla: %d\n" % self.getCasilla()
        cadena += "JUGADOR::: Energia: %d\n" % self.getEnergia()
        cadena += "JUGADOR::: Hacha: %d\n" % self.getHacha()
        cadena += "JUGADOR::: Barca: %d\n" % self.getBarca()
        cadena += "JUGADOR::: Pala: %d\n" % self.getPala()
        return cadena


    def __eq__(self, other):
        if global_vars.algoritmo == config.A_ESTRELLA or global_vars.algoritmo == config.PROFUNDIDAD or global_vars.algoritmo == config.PROFUNDIDAD_ITERATIVA:
            return self.idJugador==other.idJugador and self.equipo==other.equipo and self.casilla==other.casilla and self.hacha==other.hacha and self.barca==other.barca and self.pala==other.pala
        elif global_vars.algoritmo == config.ANCHURA:
            return self.idJugador==other.idJugador and self.equipo==other.equipo and self.casilla==other.casilla and self.energia==other.energia and self.hacha==other.hacha and self.barca==other.barca and self.pala==other.pala

