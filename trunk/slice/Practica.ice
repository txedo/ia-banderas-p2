// -*- mode: c++; coding: utf-8 -*-

#include <Ice/BuiltinSequences.ice>


module Practica {

       exception ErrorBase {
            string reason;
       };

       exception PasswordIncorrectaError extends ErrorBase {
            
       };


       exception NoExisteContrincanteError extends ErrorBase {

       };


       exception NoExistePartidaError extends ErrorBase {
	 
       };
       
       exception UsuarioIncorrectoError extends ErrorBase {
	 
       };
       
       exception MapaNoExisteError extends ErrorBase {
	 
       };
       
       exception MovimientoIncorrectoError extends ErrorBase {

       };

       struct Jugador {
	 int casilla;
	 int energia;       
	 int equipo;
	 int idJugador;
       };
       
       sequence<Jugador> JugadorSeq;
       
       struct Mapa {
	 int idUsuario;
	 Ice::IntSeq casillas;
	 JugadorSeq jugadores;
	 int dimx;
	 int dimy;
       };
       
       struct Movimiento {
	 int idJugador;
	 int mov;
       };
       
       struct InfoJugada {
	 int resultado;
	 int token;
	 bool primeraPartida;
	 Movimiento mov;
       };
       
       interface Partida {       
	 bool jugada(int idUsuario, int idJugador, int idCasilla, int token) throws MovimientoIncorrectoError;
	 Mapa obtenerMapa(string dni) throws MapaNoExisteError;
	 InfoJugada pedirTurno (int idUsuario);	 
       };
       
       interface Autenticacion {
	 Partida* login (string dni, string password) throws PasswordIncorrectaError, UsuarioIncorrectoError, NoExisteContrincanteError, NoExistePartidaError;       	
	 void finalizarPartida(string dni, string password);
       };
};
