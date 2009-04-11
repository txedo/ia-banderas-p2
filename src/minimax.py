import copy, psyco


psyco.full()


class MiniMax:
    def __init__(self, nodo_inicial):
        self.nodoInicial = nodo_inicial
        self.nodoMejor = nodo_inicial
        self.timeout = False
    
    
    def decision-minimax():
        limite = 0
        # TODO poner otra condicin por si la busqueda finaliza antes que el timeout
        while not self.timeout:
            max-valor(self.nodoInicial, limite, -INFINITO, INFINITO)
            limite += 1
    
    
    def max-valor(nodo, limite, alfa, beta):
        if test-terminal (nodo, limite, global_vars.MAX):
            return evaluacion()
        else:
            v = -INFINITO
            sucesores = expandir (nodo, global_vars.MAX)
            
            for s in sucesores:
                v = max(v, min-valor (s, alfa, beta))
                # Asignamos al nodo MAX el mayor valor de utilidad de sus hijos
                nodo.utilidad = v
                # Elegimos el mejor nodo de profundidad 1 (primer movimiento de MAX)
                if nodo.profundidad == 1:
                    if nodo > self.nodoMejor: self.nodoMejor = copy.deepcopy(nodo)
                if v >= beta:
                    return v
                alfa = max (alfa, v)
            return v
    
    
    def min-valor():
        if test-terminal (nodo, limite, global_vars.MIN):
            return evaluacion()
        else:
            v = INFINITO
            sucesores = expandir (nodo, global_vars.MIN)
            
            for s in sucesores:
                v = min(v, max-valor (s, alfa, beta))
                # Asignamos al nodo MIN el menor valor de utilidad de sus hijos
                nodo.utilidad = v
                if v <= alfa:
                    return v
                beta = min (beta, v)
            return v
                    
                    
    
    def expandir():
    
    
    def test-terminal (nodo, limite, equipo):
        terminal = True
        # Comprueba si quedan banderas en el tabero, si se ha llegado a la profundidad
        #de corte (prof. iterativa) o si se ha acabado el tiempo
        if nodo.estado.esSolucion() or nodo.profundidad==limite or self.timeout: terminal = True
        else: # Si no se cumple nada de lo anterior, miramos si quedan jugadores vivos
            for jug in nodo.estado[equipo].jugadores:
                if jug.energia > 0:
                    terminal = False
                    break
        return terminal

    
    def evaluacion():
        #tiene que guardar la utilidad en nodo.utilidad
