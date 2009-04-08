# **********************************************************************
#
# Copyright (c) 2003-2008 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.0
# Generated from file `Practica.ice'

import Ice, IcePy, __builtin__
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Practica
_M_Practica = Ice.openModule('Practica')
__name__ = 'Practica'

if not _M_Practica.__dict__.has_key('ErrorBase'):
    _M_Practica.ErrorBase = Ice.createTempClass()
    class ErrorBase(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Practica::ErrorBase'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_ErrorBase = IcePy.defineException('::Practica::ErrorBase', ErrorBase, (), None, (('reason', (), IcePy._t_string),))
    ErrorBase.ice_type = _M_Practica._t_ErrorBase

    _M_Practica.ErrorBase = ErrorBase
    del ErrorBase

if not _M_Practica.__dict__.has_key('PasswordIncorrectaError'):
    _M_Practica.PasswordIncorrectaError = Ice.createTempClass()
    class PasswordIncorrectaError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::PasswordIncorrectaError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_PasswordIncorrectaError = IcePy.defineException('::Practica::PasswordIncorrectaError', PasswordIncorrectaError, (), _M_Practica._t_ErrorBase, ())
    PasswordIncorrectaError.ice_type = _M_Practica._t_PasswordIncorrectaError

    _M_Practica.PasswordIncorrectaError = PasswordIncorrectaError
    del PasswordIncorrectaError

if not _M_Practica.__dict__.has_key('NoExisteContrincanteError'):
    _M_Practica.NoExisteContrincanteError = Ice.createTempClass()
    class NoExisteContrincanteError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::NoExisteContrincanteError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_NoExisteContrincanteError = IcePy.defineException('::Practica::NoExisteContrincanteError', NoExisteContrincanteError, (), _M_Practica._t_ErrorBase, ())
    NoExisteContrincanteError.ice_type = _M_Practica._t_NoExisteContrincanteError

    _M_Practica.NoExisteContrincanteError = NoExisteContrincanteError
    del NoExisteContrincanteError

if not _M_Practica.__dict__.has_key('NoExistePartidaError'):
    _M_Practica.NoExistePartidaError = Ice.createTempClass()
    class NoExistePartidaError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::NoExistePartidaError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_NoExistePartidaError = IcePy.defineException('::Practica::NoExistePartidaError', NoExistePartidaError, (), _M_Practica._t_ErrorBase, ())
    NoExistePartidaError.ice_type = _M_Practica._t_NoExistePartidaError

    _M_Practica.NoExistePartidaError = NoExistePartidaError
    del NoExistePartidaError

if not _M_Practica.__dict__.has_key('UsuarioIncorrectoError'):
    _M_Practica.UsuarioIncorrectoError = Ice.createTempClass()
    class UsuarioIncorrectoError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::UsuarioIncorrectoError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_UsuarioIncorrectoError = IcePy.defineException('::Practica::UsuarioIncorrectoError', UsuarioIncorrectoError, (), _M_Practica._t_ErrorBase, ())
    UsuarioIncorrectoError.ice_type = _M_Practica._t_UsuarioIncorrectoError

    _M_Practica.UsuarioIncorrectoError = UsuarioIncorrectoError
    del UsuarioIncorrectoError

if not _M_Practica.__dict__.has_key('MapaNoExisteError'):
    _M_Practica.MapaNoExisteError = Ice.createTempClass()
    class MapaNoExisteError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::MapaNoExisteError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_MapaNoExisteError = IcePy.defineException('::Practica::MapaNoExisteError', MapaNoExisteError, (), _M_Practica._t_ErrorBase, ())
    MapaNoExisteError.ice_type = _M_Practica._t_MapaNoExisteError

    _M_Practica.MapaNoExisteError = MapaNoExisteError
    del MapaNoExisteError

if not _M_Practica.__dict__.has_key('MovimientoIncorrectoError'):
    _M_Practica.MovimientoIncorrectoError = Ice.createTempClass()
    class MovimientoIncorrectoError(_M_Practica.ErrorBase):
        def __init__(self, reason=''):
            _M_Practica.ErrorBase.__init__(self, reason)

        def ice_name(self):
            return 'Practica::MovimientoIncorrectoError'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Practica._t_MovimientoIncorrectoError = IcePy.defineException('::Practica::MovimientoIncorrectoError', MovimientoIncorrectoError, (), _M_Practica._t_ErrorBase, ())
    MovimientoIncorrectoError.ice_type = _M_Practica._t_MovimientoIncorrectoError

    _M_Practica.MovimientoIncorrectoError = MovimientoIncorrectoError
    del MovimientoIncorrectoError

if not _M_Practica.__dict__.has_key('Jugador'):
    _M_Practica.Jugador = Ice.createTempClass()
    class Jugador(object):
        def __init__(self, casilla=0, energia=0):
            self.casilla = casilla
            self.energia = energia

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.casilla)
            _h = 5 * _h + __builtin__.hash(self.energia)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.casilla < other.casilla:
                return -1
            elif self.casilla > other.casilla:
                return 1
            if self.energia < other.energia:
                return -1
            elif self.energia > other.energia:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_Jugador)

        __repr__ = __str__

    _M_Practica._t_Jugador = IcePy.defineStruct('::Practica::Jugador', Jugador, (), (
        ('casilla', (), IcePy._t_int),
        ('energia', (), IcePy._t_int)
    ))

    _M_Practica.Jugador = Jugador
    del Jugador

if not _M_Practica.__dict__.has_key('_t_JugadorSeq'):
    _M_Practica._t_JugadorSeq = IcePy.defineSequence('::Practica::JugadorSeq', (), _M_Practica._t_Jugador)

if not _M_Practica.__dict__.has_key('Mapa'):
    _M_Practica.Mapa = Ice.createTempClass()
    class Mapa(object):
        def __init__(self, casillas=None, jugadores=None, dimx=0, dimy=0):
            self.casillas = casillas
            self.jugadores = jugadores
            self.dimx = dimx
            self.dimy = dimy

        def __hash__(self):
            _h = 0
            if self.casillas:
                for _i0 in self.casillas:
                    _h = 5 * _h + __builtin__.hash(_i0)
            if self.jugadores:
                for _i1 in self.jugadores:
                    _h = 5 * _h + __builtin__.hash(_i1)
            _h = 5 * _h + __builtin__.hash(self.dimx)
            _h = 5 * _h + __builtin__.hash(self.dimy)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.casillas < other.casillas:
                return -1
            elif self.casillas > other.casillas:
                return 1
            if self.jugadores < other.jugadores:
                return -1
            elif self.jugadores > other.jugadores:
                return 1
            if self.dimx < other.dimx:
                return -1
            elif self.dimx > other.dimx:
                return 1
            if self.dimy < other.dimy:
                return -1
            elif self.dimy > other.dimy:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_Mapa)

        __repr__ = __str__

    _M_Practica._t_Mapa = IcePy.defineStruct('::Practica::Mapa', Mapa, (), (
        ('casillas', (), _M_Ice._t_IntSeq),
        ('jugadores', (), _M_Practica._t_JugadorSeq),
        ('dimx', (), IcePy._t_int),
        ('dimy', (), IcePy._t_int)
    ))

    _M_Practica.Mapa = Mapa
    del Mapa

if not _M_Practica.__dict__.has_key('Movimiento'):
    _M_Practica.Movimiento = Ice.createTempClass()
    class Movimiento(object):
        def __init__(self, idJugador=0, mov=0):
            self.idJugador = idJugador
            self.mov = mov

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.idJugador)
            _h = 5 * _h + __builtin__.hash(self.mov)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.idJugador < other.idJugador:
                return -1
            elif self.idJugador > other.idJugador:
                return 1
            if self.mov < other.mov:
                return -1
            elif self.mov > other.mov:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_Movimiento)

        __repr__ = __str__

    _M_Practica._t_Movimiento = IcePy.defineStruct('::Practica::Movimiento', Movimiento, (), (
        ('idJugador', (), IcePy._t_int),
        ('mov', (), IcePy._t_int)
    ))

    _M_Practica.Movimiento = Movimiento
    del Movimiento

if not _M_Practica.__dict__.has_key('InfoJugada'):
    _M_Practica.InfoJugada = Ice.createTempClass()
    class InfoJugada(object):
        def __init__(self, resultado=0, token=0, primeraPartida=False, mov=_M_Practica.Movimiento()):
            self.resultado = resultado
            self.token = token
            self.primeraPartida = primeraPartida
            self.mov = mov

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.resultado)
            _h = 5 * _h + __builtin__.hash(self.token)
            _h = 5 * _h + __builtin__.hash(self.primeraPartida)
            _h = 5 * _h + __builtin__.hash(self.mov)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.resultado < other.resultado:
                return -1
            elif self.resultado > other.resultado:
                return 1
            if self.token < other.token:
                return -1
            elif self.token > other.token:
                return 1
            if self.primeraPartida < other.primeraPartida:
                return -1
            elif self.primeraPartida > other.primeraPartida:
                return 1
            if self.mov < other.mov:
                return -1
            elif self.mov > other.mov:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_InfoJugada)

        __repr__ = __str__

    _M_Practica._t_InfoJugada = IcePy.defineStruct('::Practica::InfoJugada', InfoJugada, (), (
        ('resultado', (), IcePy._t_int),
        ('token', (), IcePy._t_int),
        ('primeraPartida', (), IcePy._t_bool),
        ('mov', (), _M_Practica._t_Movimiento)
    ))

    _M_Practica.InfoJugada = InfoJugada
    del InfoJugada

if not _M_Practica.__dict__.has_key('Partida'):
    _M_Practica.Partida = Ice.createTempClass()
    class Partida(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Practica.Partida:
                raise RuntimeError('Practica.Partida is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Practica::Partida')

        def ice_id(self, current=None):
            return '::Practica::Partida'

        def ice_staticId():
            return '::Practica::Partida'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def jugada(self, idUsuario, idJugador, idCasilla, token, current=None):
        # def obtenerMapa(self, current=None):
        # def pedirTurno(self, idUsuario, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_Partida)

        __repr__ = __str__

    _M_Practica.PartidaPrx = Ice.createTempClass()
    class PartidaPrx(Ice.ObjectPrx):

        def jugada(self, idUsuario, idJugador, idCasilla, token, _ctx=None):
            return _M_Practica.Partida._op_jugada.invoke(self, ((idUsuario, idJugador, idCasilla, token), _ctx))

        def obtenerMapa(self, _ctx=None):
            return _M_Practica.Partida._op_obtenerMapa.invoke(self, ((), _ctx))

        def pedirTurno(self, idUsuario, _ctx=None):
            return _M_Practica.Partida._op_pedirTurno.invoke(self, ((idUsuario, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Practica.PartidaPrx.ice_checkedCast(proxy, '::Practica::Partida', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Practica.PartidaPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Practica._t_PartidaPrx = IcePy.defineProxy('::Practica::Partida', PartidaPrx)

    _M_Practica._t_Partida = IcePy.defineClass('::Practica::Partida', Partida, (), True, None, (), ())
    Partida.ice_type = _M_Practica._t_Partida

    Partida._op_jugada = IcePy.Operation('jugada', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int), ((), IcePy._t_int), ((), IcePy._t_int), ((), IcePy._t_int)), (), IcePy._t_bool, (_M_Practica._t_MovimientoIncorrectoError,))
    Partida._op_obtenerMapa = IcePy.Operation('obtenerMapa', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_Practica._t_Mapa, (_M_Practica._t_MapaNoExisteError,))
    Partida._op_pedirTurno = IcePy.Operation('pedirTurno', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int),), (), _M_Practica._t_InfoJugada, ())

    _M_Practica.Partida = Partida
    del Partida

    _M_Practica.PartidaPrx = PartidaPrx
    del PartidaPrx

if not _M_Practica.__dict__.has_key('Autenticacion'):
    _M_Practica.Autenticacion = Ice.createTempClass()
    class Autenticacion(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Practica.Autenticacion:
                raise RuntimeError('Practica.Autenticacion is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Practica::Autenticacion')

        def ice_id(self, current=None):
            return '::Practica::Autenticacion'

        def ice_staticId():
            return '::Practica::Autenticacion'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def login(self, dni, password, current=None):
        # def finalizarPartida(self, dni, password, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Practica._t_Autenticacion)

        __repr__ = __str__

    _M_Practica.AutenticacionPrx = Ice.createTempClass()
    class AutenticacionPrx(Ice.ObjectPrx):

        def login(self, dni, password, _ctx=None):
            return _M_Practica.Autenticacion._op_login.invoke(self, ((dni, password), _ctx))

        def finalizarPartida(self, dni, password, _ctx=None):
            return _M_Practica.Autenticacion._op_finalizarPartida.invoke(self, ((dni, password), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Practica.AutenticacionPrx.ice_checkedCast(proxy, '::Practica::Autenticacion', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Practica.AutenticacionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Practica._t_AutenticacionPrx = IcePy.defineProxy('::Practica::Autenticacion', AutenticacionPrx)

    _M_Practica._t_Autenticacion = IcePy.defineClass('::Practica::Autenticacion', Autenticacion, (), True, None, (), ())
    Autenticacion.ice_type = _M_Practica._t_Autenticacion

    Autenticacion._op_login = IcePy.Operation('login', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), _M_Practica._t_PartidaPrx, (_M_Practica._t_PasswordIncorrectaError, _M_Practica._t_UsuarioIncorrectoError))
    Autenticacion._op_finalizarPartida = IcePy.Operation('finalizarPartida', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), None, ())

    _M_Practica.Autenticacion = Autenticacion
    del Autenticacion

    _M_Practica.AutenticacionPrx = AutenticacionPrx
    del AutenticacionPrx

# End of module Practica
