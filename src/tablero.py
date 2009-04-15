from casilla import *
import global_vars


class Tablero:
    def __init__ (self, casillas=[], banderas=0):
        self.casillasModificadas = casillas[:]
        self.banderas=banderas
    
    
    def getCasillasModificadas(self):
        return self.casillasModificadas
    
    
    def setCasillasModificadas(self, seq):
        self.casillasModificadas.extend(seq)
    
    
    def eliminarCasillaModificada(self, casilla):
        self.casillasModificadas.remove(casilla)
    
    
    def anadirCasillaModificada(self, casilla):
        self.casillasModificadas.append(casilla)
    
    
    def IdCasillasVecinas (self, casilla):
        """ RECIBE un entero que es el identificador de la casilla para la cual
        queremos encontrar las vecinas.
            DEVUELVE una lista con los identificadores de las casillas vecinas
        dada una casilla en un tablero de casillas hexagonales
        """
        
        casillasVecinas = [-1, -1, -1, -1, -1, -1]
        columnas = global_vars.columnasTablero
        filas = global_vars.filasTablero
        cruzarAncho = filas*columnas-columnas
        if casilla > 0 and casilla <= columnas: # Primera fila
            casillasVecinas[0] = casilla + cruzarAncho
            if (casilla%2) != 0: # Primera fila e impar
                casillasVecinas[1] = casilla + cruzarAncho + 1 
                casillasVecinas[2] = casilla + 1
                casillasVecinas[3] = casilla + columnas
                if casilla == 1: # Primera fila y primera casilla
                    casillasVecinas[4] = columnas
                    casillasVecinas[5] = columnas*filas
                else: # Primera fila y resto de casillas impares
                    casillasVecinas[4] = casilla - 1
                    casillasVecinas[5] = casilla + cruzarAncho - 1
            else: # Primera fila y par
                if casilla == columnas: # Primera fila y ultima casilla(par)
                    casillasVecinas[1] = 1
                    casillasVecinas[2] = casilla + 1
                else: # Primera fila y resto de casillas pares
                    casillasVecinas[1] = casilla + 1
                    casillasVecinas[2] = casilla + columnas + 1
                casillasVecinas[3] = casilla + columnas
                casillasVecinas[4] = casilla + columnas - 1
                casillasVecinas[5] = casilla - 1
        elif casilla > cruzarAncho and casilla <= columnas*filas: # Ultima fila
            casillasVecinas[0] = casilla - columnas
            if (casilla%2) != 0: # Ultima fila e impar
                casillasVecinas[1] = casilla - columnas + 1
                casillasVecinas[2] = casilla + 1
                casillasVecinas[3] = casilla - cruzarAncho
                if casilla == cruzarAncho + 1: # Ultima fila y primera casilla (impar)
                    casillasVecinas[4] = columnas*filas
                    casillasVecinas[5] = casilla - 1
                else: # Ultima fila y resto de casillas impares
                    casillasVecinas[4] = casilla - 1
                    casillasVecinas[5] = casilla - columnas - 1
            else: # Ultima fila y par
                if casilla == columnas*filas: # Ultima fila y ultima casilla (par)
                    casillasVecinas[1] = casilla - columnas + 1
                    casillasVecinas[2] = 1
                else: # Ultima fila y resto de casillas pares
                    casillasVecinas[1] = casilla + 1
                    casillasVecinas[2] = casilla - cruzarAncho + 1
                casillasVecinas[3] = casilla - cruzarAncho
                casillasVecinas[4] = casilla - cruzarAncho - 1
                casillasVecinas[5] = casilla - 1
        else: # No es ni primera ni ultima fila
            casillasVecinas[0] = casilla - columnas
            if (casilla%2) != 0: # Impar
                casillasVecinas[1] = casilla - columnas + 1
                casillasVecinas[2] = casilla + 1
                casillasVecinas[3] = casilla + columnas
                if ((casilla-1)%columnas == 0): # Borde izquierdo
                    casillasVecinas[4] = casilla + columnas - 1
                    casillasVecinas[5] = casilla - 1
                else:
                    casillasVecinas[4] = casilla - 1
                    casillasVecinas[5] = casilla - columnas - 1
            else: # Par
                if (casilla%columnas) == 0: # Borde derecho
                    casillasVecinas[1] = casilla - columnas + 1
                    casillasVecinas[2] = casilla + 1
                else:
                    casillasVecinas[1] = casilla + 1
                    casillasVecinas[2] = casilla + columnas + 1
                casillasVecinas[3] = casilla + columnas
                casillasVecinas[4] = casilla + columnas - 1
                casillasVecinas[5] = casilla - 1
        return casillasVecinas
        
        
    def casillaActual (self, idCasilla):
        """ RECIBE un identificador de casilla
            DEVUELVE un objeto casilla con su identificador y tipo actual
        """
        cas = copy.deepcopy(global_vars.casillasIniciales[idCasilla-1])
        # Si la casilla NO es una muralla, miramos si ha sido modificada
        if cas.getTipo() != T_MURALLA:
            if cas in self.casillasModificadas:
                indice = self.casillasModificadas.index(cas)
                cas.setTipo(self.casillasModificadas[indice].getTipo())
        return cas
    
    
    def casillasVecinas (self, casillasActuales, casilla):
        """ RECIBE la lista de casillas actuales del tablero y el identificador
        de la casilla de la cual queremos obtener las casillas vecinas.
            DEVUELVE las 6 casillas vecinas en el tablero actual
        """
        # Obtenemos los identificadores de las casillas vecinas
        idVecinas = self.idCasillasVecinas(casilla)
        # Construimos las casillas vecinas actuales
        casillasVecinas = []
        for i in idVecinas:
            cas = Casilla (i, casillasActuales[i - 1].getTipo())
            casillasVecinas.append (cas)
        return casillasVecinas
    
    
    def casillasVecinasActuales (self, idCasilla):
        """ RECIBE el identificador de la casilla sobre la cual queremos calcular
        las casillas vecinas actuales.
            DEVUELVE las 6 casllas vecinas actuales
            Utilizar esta funcion es mejor que llamar a tableroActual y luego
            llamar a casillasVecinas.
        """
        # Obtenemos los identificadores de las casillas vecinas
        idVecinas = self.idCasillasVecinas(idCasilla)
        # Construimos las casillas vecinas actuales
        casillasVecinas = []
        for i in idVecinas:
            cas = Casilla (i, global_vars.casillasIniciales[i-1].getTipo())
            if cas in self.casillasModificadas:
                indice = self.casillasModificadas.index(cas)
                cas.setTipo(self.casillasModificadas[indice].getTipo())
            casillasVecinas.append(cas)
        return casillasVecinas
    
    
    def tableroActual (self):
        """ DEVUELVE una lista con las casillas del tablero actual """
        casillas = global_vars.casillasIniciales[:]
        for i in range(len(self.getCasillasModificadas())):
            casillas[self.casillasModificadas[i].getIdCasilla()-1] = self.casillasModificadas[i]
        return casillas
    
    
    def __WayTrackingBack (self, k, idCasillaDestino, calculadas, casillasTablero, distancias):
        if calculadas == filas*columnas: return
        else:
            for i in range(len(distancias)):
                if distancias[i] == k:
                    adyacentes = self.casillasVecinasActuales(i+1)
                    for j in adyacentes:
                        if j.tipo != T_MURALLA and distancias[j.idCasilla - 1] > k+1:
                            distancias[j.idCasilla - 1] = k+1
                            calculadas += 1
            self.__WayTrackingBack (k+1, idCasillaDestino, calculadas, casillasTablero, distancias)
     
     
    def WayTracking (self, idCasillaDestino):
        columnas = global_vars.columnasTablero
        filas = global_vars.filasTablero
        casillas = global_vars.casillasIniciales[:]
        # Inicializo la lista de distancias a INFINITO
        distancias = []
        for i in range(filas*columnas):
            distancias.append(INFINITO)
            #casillas.append(Casilla(i+1,1))                            #test
        #ponerMurallas(casillas)                                        #test
        # Etiqueto la casilla de la bandera con distancia 0
        calculadas = 1
        distancias[idCasillaDestino-1] = 0
        # Etiqueto las murallas con distancia -1
        for i in casillas:
            if i.tipo == T_MURALLA:
                distancias[i.idCasilla-1] = -1
                calculadas += 1
        #Imprimir (distancias)                                                   #test
        self.__WayTrackingBack(0, idCasillaDestino, calculadas, casillas, distancias)
        return distancias
    
    
    def __contains__(self, element):
        return element in self.casillasModificadas
    
    
    def __eq__(self, other):
        return self.casillasModificadas==other.casillasModificadas

