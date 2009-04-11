from config import PROF_INICIAL

class Nodo:


    def __init__ (self, estado, padre=None, accion=None, profundidad=PROF_INICIAL, utilidad=-INFINITO):
        self.estado = estado # Tipo estado
        self.padre = padre # Tipo nodo
        self.accion = accion # Tupla (jugador, accion)
        self.profundidad = profundidad # Tipo entero
        self.utilidad = utilidad
        
        
    def repetidoEnRama (self):
        """ Comprueba si el estado del nodo esta repetido en alguna de sus nodos
        antecesores (solo comprueba en su rama).
            DEVUELVE True si esta repetido; False si no esta repetido
        """
        repetido = False
        actual = self
        while not repetido and actual.profundidad > PROF_INICIAL:
            if self == actual.padre: repetido = True
            actual = actual.padre
        return repetido
        

    def __cmp__(self, other):
        return cmp(self.utilidad, other.utilidad)


    def __eq__(self, other):
        return self.estado==other.estado


    def __str__(self):
        cad = ""
        for i in self.estado.jugadores:
            cad += "Jugador " + str(i.idJugador) + "\tCasilla: " + str(i.casilla) + "\tEnergia: " + str(i.energia) + "\n"
        cad += "Accion: " + str(self.accion) + "\tCoste: " + str(self.g) + "\tProfundidad: " + str(self.profundidad)
        return cad
