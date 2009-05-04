import copy, psyco, time, global_vars, math
from config import *
from nodo import *


psyco.full()


class Minimax:
    def __init__(self, nodo_inicial):
        self.nodoInicial = nodo_inicial
        self.nodoMejor = copy.deepcopy(nodo_inicial)
        self.timeout = False
        
        
    def Sync (self):
        tiempo = 0
        self.timeout = False
        while tiempo < global_vars.deadline - SECURITY_RANGE:
            time.sleep(TIME_INCREMENT)
            tiempo += TIME_INCREMENT
        self.timeout = True
        print "Tiempo: %f" % (tiempo)
    
    
    def decision_minimax(self):
        limite = 0
        # TODO poner otra condicin por si la busqueda finaliza antes que el timeout
        while not self.timeout:
            self.max_valor(self.nodoInicial, limite, -INFINITO, INFINITO)
            limite += 1
        print limite
    
    
    def max_valor(self, nodo, limite, alfa, beta):
        if self.test_terminal (nodo, limite):
            return self.evaluacion(nodo, global_vars.MAX, global_vars.MIN)

        v = -INFINITO
        sucesores = self.expandir (nodo, global_vars.MAX)
        
        i = 0
        while not self.timeout and i < len(sucesores):
            v = max(v, self.min_valor (sucesores[i], limite, alfa, beta))
            #if not timeout????
            if v >= beta:
                return v
            alfa = max (alfa, v)
            # Asignamos al nodo MAX el mayor valor de utilidad de sus hijos
            #nodo.utilidad = v
            # Elegimos el mejor nodo de profundidad 1 (primer movimiento de MAX)
            if sucesores[i].profundidad == PROF_INICIAL+1:
                #if nodo > self.nodoMejor: self.nodoMejor = copy.deepcopy(sucesores[i])
                if v > self.nodoMejor.utilidad:
                    self.nodoMejor = copy.deepcopy(sucesores[i])
                    self.nodoMejor.utilidad = v
            i += 1                        
        return v
    
    
    def min_valor(self, nodo, limite, alfa, beta):
        if self.test_terminal (nodo, limite):
            return self.evaluacion(nodo, global_vars.MAX, global_vars.MIN)

        v = INFINITO
        sucesores = self.expandir (nodo, global_vars.MIN)
       
        i = 0
        while not self.timeout and i < len(sucesores):
            v = min(v, self.max_valor (sucesores[i], limite, alfa, beta))
            #if not timeout????
            if v <= alfa:
                return v
            beta = min (beta, v)
            # Asignamos al nodo MIN el menor valor de utilidad de sus hijos
            #nodo.utilidad = v
            i += 1
        return v
                    
                    
    
    def expandir(self, nodo, equipo):
        sucesores = []
        numero_jugadores = len(nodo.estado.equipos[equipo].jugadores)
        for jug in range(numero_jugadores):
            if nodo.estado.equipos[equipo].jugadores[jug].getEnergia() > 0:
                casillasVecinas = nodo.estado.tablero.casillasVecinasActuales(nodo.estado.equipos[equipo].jugadores[jug].getCasilla())
                # ANadimos la casilla actual para hacer hoyos
                if nodo.estado.equipos[equipo].jugadores[jug].pala > 0:
                    casillasVecinas.append(nodo.estado.tablero.casillaActual(nodo.estado.equipos[equipo].jugadores[jug].getCasilla()))
                for mov in range (len(casillasVecinas)):
                    # Comprobamos que sea la misma casilla o, si es distinta casilla que no sea muralla
                    #es decir, comprobamos que si nos movemos, la casilla destino NO sea una muralla
                    if casillasVecinas[mov].getIdCasilla() == nodo.estado.equipos[equipo].jugadores[jug].getCasilla() or casillasVecinas[mov].getTipo() != T_MURALLA:
                        estadoAux = copy.deepcopy(nodo.estado)
                        if estadoAux.actualizarEstado (equipo, jug, casillasVecinas[mov]):
                            accion = (estadoAux.equipos[equipo].jugadores[jug].getIdJugador(), mov+1)
                            nuevoNodo = Nodo (estadoAux, nodo, accion, nodo.profundidad+1)
                            sucesores.append(nuevoNodo)
        return sucesores
    
    
    def test_terminal (self, nodo, limite):
        terminal = False
        # Comprueba si quedan banderas en el tabero, si se ha llegado a la profundidad
        #de corte (prof. iterativa) o si se ha acabado el tiempo
        if nodo.estado.esSolucion() or nodo.profundidad==limite: # or self.timeout:
            terminal = True
        #else: # Si no se cumple nada de lo anterior, miramos si quedan jugadores vivos
        #    for jug in nodo.estado[equipo].jugadores:
        #        if jug.energia > 0:
        #            terminal = False
        #            break
        return terminal

    
    def evaluacion(self, nodo, equipo1, equipo2):
        estado = nodo.estado
        totalBanderas = len(global_vars.banderasObjetivo)
        
        bandEq1 = estado.equipos[equipo1].banderasCapturadas
        bandEq2 = estado.equipos[equipo2].banderasCapturadas
        
        ratioBandEq1 = bandEq1*totalBanderas#/totalBanderas
        ratioBandEq2 = bandEq2*totalBanderas#/totalBanderas
        ratioBand = ratioBandEq1 - ratioBandEq2
        ratioBand = ratioBand * 20000
        
        filas = global_vars.filasTablero
        columnas = global_vars.columnasTablero
        
        bondadDist = max(columnas,filas)/2
        (x,y,distEq1) = estado.minimaDistancia(equipo1)
        #print "distEq1: ", distEq1
        (x,y,distEq2) = estado.minimaDistancia(equipo2)
        #print "distEq2: ", distEq2
        ratioDistEq1 = bondadDist * math.exp((-1/(bondadDist/4))*distEq1)
        #print "ratioDistEq1: ", ratioDistEq1
        ratioDistEq2 = bondadDist * math.exp((-1/(bondadDist/4))*distEq2)
        #print "ratioDistEq2: ", ratioDistEq2
        ratioDist = ratioDistEq1 - ratioDistEq2
        #raw_input()
        
        ##############
        # ENERGIA
        ##############
        (jug,accion) = nodo.accion
        equipoExpande = (jug-1)//len(nodo.estado.equipos[0].jugadores)
        energiaEq1 = nodo.estado.equipos[equipoExpande].getEnergiaTotal()
        #ratioEnergiaEq1 = energiaEq1/100
        
        evalEq1 = ratioBandEq1 + ratioDistEq1# + ratioEnergiaEq1
        evalEq2 = ratioBandEq2 + ratioDistEq2
        """evaluacion = 20 * (bandEq1 - bandEq2)
        (x,y,distEq1) = estado.minimaDistancia(equipo1)
        (x,y,distEq2) = estado.minimaDistancia(equipo2)
        evaluacion += (10 * (1.0/distEq1)) - (10 * (1.0/distEq2))"""
        return evalEq1 - evalEq2
        #return evaluacion

