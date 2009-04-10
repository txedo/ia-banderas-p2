from config import PROF_INICIAL

class Nodo:


    def __init__ (self, estado, padre=None, accion=None, profundidad=PROF_INICIAL, g=0, f=0):
        self.estado = estado # Tipo estado
        self.padre = padre # Tipo nodo
        self.accion = accion # Tupla (jugador, accion)
        self.profundidad = profundidad # Tipo entero
        self.g = g # Tipo entero. Coste para llegar desde el inicio hasta el nodo actual
        self.f = f # Tipo entero. Coste total estimado para llegar desde el incio hasta el estado objetivo (Solo en A*)
        
        
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
        return cmp(self.f, other.f)


    def __eq__(self, other):
        return self.estado==other.estado


    def __str__(self):
        cad = ""
        for i in self.estado.jugadores:
            cad += "Jugador " + str(i.idJugador) + "\tCasilla: " + str(i.casilla) + "\tEnergia: " + str(i.energia) + "\n"
        cad += "Accion: " + str(self.accion) + "\tCoste: " + str(self.g) + "\tProfundidad: " + str(self.profundidad)
        return cad
