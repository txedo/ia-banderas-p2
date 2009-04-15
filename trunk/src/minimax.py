import copy, psyco, time


psyco.full()


class MiniMax:
    def __init__(self, nodo_inicial):
        self.nodoInicial = nodo_inicial
        self.nodoMejor = copy.deepcopy(nodo_inicial)
        self.timeout = False
        
        
    def Sync (self, tiempo):
        time.sleep(tiempo)
        self.timeout = True
    
    
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
            
            i = 0
            while not self.timeout and i < len(sucesores):
                v = max(v, min-valor (sucesores[i], alfa, beta))
                #if not timeout????
                if v >= beta:
                    return v
                alfa = max (alfa, v)
                # Asignamos al nodo MAX el mayor valor de utilidad de sus hijos
                #nodo.utilidad = v
                # Elegimos el mejor nodo de profundidad 1 (primer movimiento de MAX)
                if nodo.profundidad == config.PROF_INICIAL:
                    #if nodo > self.nodoMejor: self.nodoMejor = copy.deepcopy(sucesores[i])
                    if v > self.nodoMejor.utilidad:
                        self.nodoMejor = copy.deepcopy(sucesores[i])
                        self.nodoMejor.utilidad = v
                i += 1
                        
            return v
    
    
    def min-valor():
        if test-terminal (nodo, limite, global_vars.MIN):
            return evaluacion()
        else:
            v = INFINITO
            sucesores = expandir (nodo, global_vars.MIN)
            
            i = 0
            while not self.timeout and i < len(sucesores):
                v = min(v, max-valor (sucesores[i], alfa, beta))
                #if not timeout????
                if v <= alfa:
                    return v
                beta = min (beta, v)
                # Asignamos al nodo MIN el menor valor de utilidad de sus hijos
                #nodo.utilidad = v
                i += 1
            return v
                    
                    
    
    def expandir(nodo, equipo):
        sucesores = []
        numero_jugadores = len(nodo.estado.equipos[equipo].jugadores)
        for jug in range(numero_jugadores):
            if nodo.estado.equipos[equipo].jugadores[jug].getEnergia() > 0:
                casillasVecinas = nodo.estado.tablero.casillasVecinasActuales(nodo.estado.equipos[equipo].jugadores[jug].getCasilla())
                # Añadimos la casilla actual para hacer hoyos
                casillasVecinas.append(nodo.estado.tablero.casillaActual(nodo.estado.equipos[equipo].jugadores[jug].getCasilla()))
                for mov in range (idCasillasVecinas):
                    # Comprobamos que sea la misma casilla o, si es distinta casilla que no sea muralla
                    #es decir, comprobamos que si nos movemos, la casilla destino NO sea una muralla
                    if casillasVecinas[mov].getIdCasilla() == nodo.estado.equipos[equipo].jugadores[jug].getCasilla() or casillasVecinas[mov].getTipo() != T_MURALLA:
                        estadoAux = copy.deepcopy(nodo.estado)
                        if estadoAux.actualizarEstado (equipo, jug, casillasVecinas[mov]):
                            accion = (estadoAux.equipos[equipo].jugadores[jug].getIdJugador(), mov+1)
                            nuevoNodo = Nodo (estadoAux, nodo, accion, nodo.profundidad+1)
                            sucesores.append(nuevoNodo)
        return sucesores
    
    
    def test-terminal (nodo, limite, equipo):
        terminal = False
        # Comprueba si quedan banderas en el tabero, si se ha llegado a la profundidad
        #de corte (prof. iterativa) o si se ha acabado el tiempo
        if nodo.estado.esSolucion() or nodo.profundidad==limite or self.timeout: terminal = True
        #else: # Si no se cumple nada de lo anterior, miramos si quedan jugadores vivos
        #    for jug in nodo.estado[equipo].jugadores:
        #        if jug.energia > 0:
        #            terminal = False
        #            break
        return terminal

    
    def evaluacion():
        #tiene que guardar la utilidad en nodo.utilidad
