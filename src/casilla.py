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
            
    
    def coste (self, hacha, barca):
        tieneHacha = False
        tieneBarca = False
        if hacha > 0: tieneHacha = True
        if barca > 0: tieneBarca = True
        if self.tipo == T_HIERBA or self.tipo == T_BANDERA or self.tipo == T_PALA or self.tipo == T_BARCA or self.tipo == T_HACHA or self.tipo == T_ZUMO:
            return 1
        elif self.tipo == T_AGUA:
            if tieneBarca: return 3
            else: return 6
        elif self.tipo == T_BOSQUE:
            if tieneHacha: return 4
            else: return 8
        elif self.tipo == T_BARRO: return 2
        elif self.tipo == T_HOYO: return 4
        elif self.tipo == T_ZANJA: return 6
        
     
    def __eq__(self, other):
        return self.idCasilla==other.idCasilla
        
        
    def __str__(self):
        cadena = "CASILLA::: Id: %d\n" % self.getIdCasilla()
        cadena += "CASILLA::: Tipo: %d\n" % self.getTipo()
        return cadena

