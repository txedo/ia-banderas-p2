from config import *


class Estado:


    def __init__ (self, tablero, equipos):
        self.tablero = tablero
        self.equipos = equipos
        
        
    def esSolucion (self):
        if self.tablero.banderas==0: return True
        else: return False
        

    def actualizarEstado (self, eq, jug, casillaDestino):
        """ Actualiza las componentes del estado: tablero y jugadores.
        Del tablero se actualizan las casillas modificadas (si se ha modificado
        alguna) y de los jugadores se actualizan la vida y los objetos.
            RECIBE "jug" que es el indice del jugador en la lista de jugadores
        (normalmente idJugador-1) y la casilla a la que se mueve (tipo Casilla)
            DEVUELVE nada.
        """
        equipoActor = self.equipos[eq]
        jugadorActor = self.equipos[eq].jugadores[jug]
        accionEjecutada = True
        if jugadorActor.getCasilla() <> casillaDestino.getIdCasilla(): # El jugador se mueve
            self.equipos[eq].jugadores[jug].setCasilla(casillaDestino.getIdCasilla())
            # Dirty indica si es necesario actualizar las casillas modificadas del tablero
            dirty = 0
            if casillaDestino.getTipo() == T_HIERBA:
                accionEjecutada = jugadorActor.perderEnergia(1)
            elif casillaDestino.getTipo() == T_AGUA:
                accionEjecutada = jugadorActor.usarBarca()
            elif casillaDestino.getTipo() == T_BARRO:
                accionEjecutada = jugadorActor.perderEnergia(2)
            elif casillaDestino.getTipo() == T_HOYO:
                accionEjecutada = jugadorActor.perderEnergia(4)
            elif casillaDestino.getTipo() == T_ZANJA:
                accionEjecutada = jugadorActor.perderEnergia(6)
            elif casillaDestino.getTipo() == T_BANDERA:
                dirty = 1
                jugadorActor.cogerBandera()
                equipoActor.capturarBandera()
                self.tablero.banderas -= 1
            elif casillaDestino.getTipo() == T_BARCA:
                dirty = 1
                jugadorActor.cogerBarca()
            elif casillaDestino.getTipo() == T_HACHA:
                dirty = 1
                jugadorActor.cogerHacha()
            elif casillaDestino.getTipo() == T_ZUMO:
                dirty = 1
                jugadorActor.beberZumo()
            elif casillaDestino.getTipo() == T_PALA:
                dirty = 1
                jugadorActor.cogerPala()
            elif casillaDestino.getTipo() == T_BOSQUE:
                (accionEjecutada, hacha) = jugadorActor.usarHacha()
                if accionEjecutada and hacha: dirty = 1
            # Si el dirty bit vale 1, actualizamos la casilla
            if dirty == 1:
                 casillaDestino.convertirHierba()
                 self.tablero.anadirCasillaModificada(casillaDestino)
        else: # El jugador no se mueve utiliza la pala
            if jugadorActor.usarPala(): # El jugador tiene pala para usarla satisfactoriamente
                if casillaDestino in self.tablero.getCasillasModificadas():
                    self.tablero.eliminarCasillaModificada(casillaDestino)
                casillaDestino.cavar()
                self.tablero.anadirCasillaModificada(casillaDestino)
            else: # El jugador NO tiene pala, por lo que no puede ejecutar la accion
                accionEjecutada = False
        return accionEjecutada
            
    
    def __eq__(self, other):
        return self.tablero==other.tablero and self.jugadores==other.jugadores
        
