from config import *
import psyco

psyco.full()

class Casilla:
    def __init__ (self, idCasilla, tipo):
        self.idCasilla = idCasilla
        self.tipo = tipo
        
        
    def setIdCasilla (self, idCasilla):
        self.idCasilla = idCasilla
        
        
    def getIdCasilla (self):
        return self.idCasilla
        
        
    def setTipo (self, tipo):
        self.tipo = tipo
        
        
    def getTipo (self):
        return self.tipo
        
    
    def convertirHierba (self):
        self.setTipo (T_HIERBA)
            
                
    def cavar (self):
        if self.getTipo() == T_HOYO: self.setTipo (T_ZANJA)
        else:
            if self.getTipo() <> T_ZANJA: self.setTipo (T_HOYO)
        
     
    def __eq__(self, other):
        return self.idCasilla==other.idCasilla
        
        
    def __str__(self):
        cadena = "CASILLA::: Id: %d\n" % self.getIdCasilla()
        cadena += "CASILLA::: Tipo: %d\n" % self.getTipo()
        return cadena

