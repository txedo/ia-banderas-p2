import copy, psyco, time, global_vars, math, random
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
        limite = 1
        while not self.timeout:
            self.max_valor(self.nodoInicial, limite, -INFINITO, INFINITO)
            limite += 1
        print "Profundidad alcanzada: ", limite
    
    
    def max_valor(self, nodo, limite, alfa, beta):
        if self.test_terminal (nodo, limite):
            return self.evaluacion(nodo, global_vars.MAX, global_vars.MIN)

        v = -INFINITO
        sucesores = self.expandir (nodo, global_vars.MAX)
        
        i = 0
        while not self.timeout and i < len(sucesores):
            v = max(v, self.min_valor (sucesores[i], limite, alfa, beta))
            # Poda
            if v >= beta:
                return v
            alfa = max (alfa, v)
            # Si no hemos podado, comprobamos la utilidad del nodo y
            # si es el mejor nodo que hemos encontrado hasta ahora
            # seleccionamos su antecesor con profundidad 1
            if v > self.nodoMejor.utilidad:
                self.nodoMejor = copy.deepcopy(sucesores[i].primerAntecesor())
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
            if v <= alfa:
                return v
            beta = min (beta, v)
            i += 1
        return v
                    
                    
    
    def expandir(self, nodo, equipo):
        sucesores = []
        numero_jugadores = len(nodo.estado.equipos[equipo].jugadores)
        for jug in range(numero_jugadores):
            if nodo.estado.equipos[equipo].jugadores[jug].getEnergia() > 0:
                casillasVecinas = nodo.estado.tablero.casillasVecinasActuales(nodo.estado.equipos[equipo].jugadores[jug].getCasilla())
                # Si el jugador tiene pala, anadimos la casilla actual para hacer hoyos
                # Esto solo se lleva a cabo si la heuristica tiene en cuenta la energia del equipo contrario
                if nodo.estado.equipos[equipo].jugadores[jug].pala > 0:
                    casillasVecinas.append(nodo.estado.tablero.casillaActual(nodo.estado.equipos[equipo].jugadores[jug].getCasilla()))
                for mov in range (len(casillasVecinas)):
                    # Comprobamos que la casilla destino NO sea una muralla
                    if casillasVecinas[mov].getTipo() != T_MURALLA:
                        estadoAux = copy.deepcopy(nodo.estado)
                        # actualizarEstado devuelve True o False en funcion de si se ha podido ejecutar la accion o no
                        if estadoAux.actualizarEstado (equipo, jug, casillasVecinas[mov]):
                            # Si se ha podido ejecutar la accion, construimos un nuevo sucesor
                            accion = (estadoAux.equipos[equipo].jugadores[jug].getIdJugador(), mov+1)
                            nuevoNodo = Nodo (estadoAux, nodo, accion, nodo.profundidad+1)
                            sucesores.append(nuevoNodo)
        return sucesores
    
    
    def test_terminal (self, nodo, limite):
        terminal = False
        # El test-terminal solo comprueba si quedan banderas en el tabero
        # o si se ha llegado a la profundidad de corte (prof. iterativa)
        if nodo.estado.esSolucion() or nodo.profundidad==limite:
            terminal = True
        # No se comprueban energias ya que expandir() se encarga de ello
        return terminal

    
    def evaluacion(self, nodo, equipo1, equipo2):
        estado = nodo.estado
        totalBanderas = len(global_vars.banderasObjetivo)
        filas = global_vars.filasTablero
        columnas = global_vars.columnasTablero
        
        bandEq1 = estado.equipos[equipo1].banderasCapturadas
        bandEq2 = estado.equipos[equipo2].banderasCapturadas
        
        # Se toma como bondadBanderas el producto de filas*columnas para evitar
        #que en un tablero muy grande las distancias sean mas importantes que
        #las banderas.
        bondadBanderas = filas*columnas
        ratioBandEq1 = bandEq1*totalBanderas
        ratioBandEq2 = bandEq2*totalBanderas
        ratioBand = bondadBanderas * (ratioBandEq1 - ratioBandEq2)
                
        maxDist = ((columnas+filas)/2)*(3/4)
        done = False
        blacklist = []
        (jug1,band1,distEq1) = estado.minimaDistancia(equipo1)
        (jug2,band2,distEq2) = estado.minimaDistancia(equipo2)
        
        # Si el estado no es solucion y aun quedan banderas por coger
        if not estado.esSolucion():
            while not done:
                # Si la distancia mas corta del equipo MAX y MIN se refieren
                #a la misma bandera, y MIN esta mas cerca que MAX, buscamos otra
                #bandera para MAX que pueda coger sin que MIN se la quite
                if (band1 == band2) and (distEq1 > distEq2):
                    blacklist.append(band1)
                    # Actualizamos el estado eliminando la bandera que hemos metido en blacklist
                    cas = estado.tablero.casillaActual(band1)
                    cas.convertirHierba()
                    estado.tablero.anadirCasillaModificada(cas)
                    estado.tablero.banderas -= 1
                    # Si todas las banderas estan en la blacklist, quitamos una aleatoria
                    if estado.tablero.banderas == 0:
                        if len(blacklist) <= 1: white = 0
                        else: white = random.randint(1, len(blacklist)-1)
                        toDel = blacklist.pop(white)
                        casDel = estado.tablero.casillaActual(toDel)
                        estado.tablero.eliminarCasillaModificada(casDel)
                        estado.tablero.banderas += 1
                        done = True
                    # Medimos la distancia minima del equipo MAX
                    (jug1,band1,distEq1) = estado.minimaDistancia(equipo1)
                else:
                    done = True
        # Vaciamos la blacklist y ponemos el estado como estaba
        if len(blacklist) > 0:
            for i in range(len(blacklist)):
                toDel = blacklist.pop(0)
                casDel = estado.tablero.casillaActual(toDel)
                estado.tablero.eliminarCasillaModificada(casDel)
                estado.tablero.banderas += 1
        
        ratioDistEq1 = maxDist - distEq1
        ratioDistEq2 = maxDist - distEq2
        ratioDist = ratioDistEq1 - ratioDistEq2
        
        ##############
        # ENERGIA
        ##############
        #(jug,accion) = nodo.accion
        #equipoExpande = (jug-1)//len(nodo.estado.equipos[0].jugadores)
        #energiaEq1 = nodo.estado.equipos[equipoExpande].getEnergiaTotal()
        #ratioEnergiaEq1 = energiaEq1/100
        
        #evalEq1 = ratioBandEq1 + ratioDistEq1 # + ratioEnergiaEq1
        #evalEq2 = ratioBandEq2 + ratioDistEq2
        return ratioBand + ratioDist

