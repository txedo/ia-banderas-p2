import global_vars


class Init:
    def __init__(self, mapa, equipos, tablero):
        # ID de usuario
        global_vars.idUsuario = mapa.idUsuario
        # Filas y columnas del tablero
        global_vars.filasTablero = mapa.dimy
        global_vars.columnasTablero = mapa.dimx
        # Inicializamos las casillas iniciales que nos da el servidor
        for index,casilla in enumerate(mapa.casillas):
            cas = Casilla(index+1,casilla)
            global_vars.casillasIniciales.append(cas)
            if casilla == T_BANDERA:
                tablero.banderas += 1
                global_vars.banderasObjetivo.append(index+1)
        
        
