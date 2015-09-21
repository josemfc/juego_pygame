#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from Luchador import *
from Criaturas import *


def main():

	pygame.init()
	reloj = pygame.time.Clock()

	# Inicializar ventana
	Ventana = pygame.display.set_mode((807, 300))
	pygame.display.set_caption("Kung fu vs zombies")

	# Inicializar fondo
	Fondo = pygame.image.load("img/city.png")
	Fondo1 = pygame.image.load("img/fondo_negro.png")

	# Inicializar sonidos
	al_aire = pygame.mixer.Sound("sonidos/punch-air.wav")
	punio = pygame.mixer.Sound("sonidos/punch.wav")
	patada = pygame.mixer.Sound("sonidos/kung-fu-kick.wav")
	ouch = pygame.mixer.Sound("sonidos/ouch.wav")
	muerte_esq  = pygame.mixer.Sound("sonidos/bones-2.wav")
	Musica = pygame.mixer.Sound("sonidos/Final-Castle.wav")
	Musica.play(-1)

	# Inicializar fuente
	Fuente = pygame.font.Font(None, 40)
	GameOver1 = Fuente.render("GAME OVER", 0, (255,0,0))
	GameOver2 = Fuente.render("Pulse 'r' para reintentar o 'Esc' para salir", 0, (255,0,0))
	MejoresP = Fuente.render("Mejores puntuaciones: ", 0, (0,255,0))
	Mensaje = Fuente.render("Wow, has conseguido escapar!", 0, (0,0,255))

	incrementoX = 0
	muerto = False
	puntuacion = 0
	primera_partida = True
	mejores_puntuaciones = [0] * 5	# Puntuaciones
	MejoresPunt = [0] * 5	# Textos


	while True:

		if not muerto: 	# Inicializamos 
			vida = 100
			puntuacion = 0
			mensj = False

			# Inicializar luchador
			coordX = 100
			coordY = 230
			coordenadas_luchador = (coordX, coordY)
			accion = 'quieto'

			# Inicializar criaturas
			coordX_uk = 0
			coordY_uk = 230
			coordenadas_uk = (coordX_uk, coordY_uk)

			coordX_bat = 900
			coordY_bat = 180
			coordenadas_bat = (coordX_bat, coordY_bat)

			coordX_bat2 = 700
			coordY_bat2 = 180
			coordenadas_bat2 = (coordX_bat2, coordY_bat2)

			coordX_zom = 800
			coordY_zom = 230
			coordenadas_zom = (coordX_zom, coordY_zom)

			coordX_esq = 600
			coordY_esq = 230
			coordenadas_esq = (coordX_esq, coordY_esq)

			if primera_partida:		# Si es la primera partida, crear objetos
				ElLuchador = Luchador(coordenadas_luchador)
				UndeadK = UndeadKing(coordenadas_uk)
				Murcielago = Bat(coordenadas_bat, 1)
				Murcielago2 = Bat(coordenadas_bat, 2)
				Zombie = Zombiesqueleto(coordenadas_zom, 1)
				Esqueleto = Zombiesqueleto(coordenadas_esq, 2)
				primara_partida = False


		### Bucle de la partida
		while not muerto:

			# Actualizar personajes
			ElLuchador.update(coordenadas_luchador, accion)
			UndeadK.update(coordenadas_uk)
			Murcielago.update(coordenadas_bat)
			Murcielago2.update(coordenadas_bat2)
			Zombie.update(coordenadas_zom)
			Esqueleto.update(coordenadas_esq)

			# Puntuacion y vida
			Punt = Fuente.render("Puntuacion: " + str(puntuacion), 0, (0,255,0))
			Vid = Fuente.render("Vida: " + str(vida), 0, (255,0,0))

			# Poner en la ventana
			Ventana.blit(Fondo1, (0, 0))
			Ventana.blit(Fondo, (0, 0))
			Ventana.blit(Vid, (5, 5))
			Ventana.blit(Punt, (200, 5))
			Ventana.blit(UndeadK.image, UndeadK.rect)
			Ventana.blit(Murcielago.image, Murcielago.rect)
			Ventana.blit(Murcielago2.image, Murcielago2.rect)
			Ventana.blit(Zombie.image, Zombie.rect)
			Ventana.blit(Esqueleto.image, Esqueleto.rect)
			Ventana.blit(ElLuchador.image, ElLuchador.rect)

			pygame.display.flip()	# Mostrar

			# Eventos
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:	# Salir cerrando la ventana
					sys.exit()

				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:	# Salir pusando ESC
						sys.exit()
					elif evento.key == pygame.K_RIGHT and ElLuchador.accion_terminada:	# Correr a la derecha
						incrementoX = 10
						accion = 'correr'
					elif evento.key == pygame.K_LEFT and ElLuchador.accion_terminada:	# Correr a la izquierda
						incrementoX = -10
						accion = 'correr'
					elif evento.key == pygame.K_a and ElLuchador.accion_terminada:		# Botón 'a' (puño)
						ElLuchador.accion_terminada = False
						ElLuchador.anim = 0
						accion = 'puño'
						al_aire.play(0)
					elif evento.key == pygame.K_s and ElLuchador.accion_terminada:		# Botón 's' (patada)
						ElLuchador.accion_terminada = False
						ElLuchador.anim = 0
						accion = 'patada'
						al_aire.play(0)
					elif evento.key == pygame.K_d and ElLuchador.accion_terminada:		# Botón 'd' (patada alta)
						ElLuchador.accion_terminada = False
						ElLuchador.anim = 0
						accion = 'patada_alta'
						al_aire.play(0)

				if evento.type == pygame.KEYUP and ElLuchador.accion_terminada:		# Teclas levantadas (quieto)
					incrementoX = 0
					accion = 'quieto'

			# Coordenadas del Luchador (se aumentan si corre y no se sale de la pantalla)
			if accion == 'correr' and not (coordX <= 0 and incrementoX < 0) and not (coordX >= 800 and incrementoX > 0):
				coordX = coordX + incrementoX

			if coordX >= 800:						# Si llega al final, gana
				mensj = True
				muerto = True
				puntuacion = puntuacion + 2000

			coordenadas_luchador = (coordX, coordY)

			# Colisiones
			# Colisión Undead King	(Invulnerable, ElLuchador muere automáticamente)
			if pygame.sprite.collide_rect(ElLuchador, UndeadK):
				ouch.play(0)
				vida = 0
				muerto = True
			else:								# Avanzar
				coordX_uk = coordX_uk + 3
				if coordX_uk > 807:
					coordenadas_uk = 0
				coordenadas_uk = (coordX_uk, coordY_uk)

			# Colisión con murciélago (Sólo muere con patada alta)
			if pygame.sprite.collide_rect(ElLuchador, Murcielago):
				if accion == 'patada_alta':					# ElLuchador golpea
					patada.play(0)
					puntuacion = puntuacion + 20
					coordX_bat = 950
					coordenadas_bat = (coordX_bat, coordY_bat)
				else:										# ElLuchador recibe golpe
					ouch.play(0)
					vida = vida - 10
					if vida <= 0:
						muerto = True
			else:											# Si no colisiona, avanza
				coordX_bat = coordX_bat - 10
				if coordX_bat < 0:
					coordX_bat = 950
				coordenadas_bat = (coordX_bat, coordY_bat)	

			# Colisión con murciélago 2
			if pygame.sprite.collide_rect(ElLuchador, Murcielago2):
				if accion == 'patada_alta':
					patada.play(0)
					puntuacion = puntuacion + 20
					coordX_bat2 = 950
					coordenadas_bat2 = (coordX_bat2, coordY_bat2)
				else:
					ouch.play(0)
					vida = vida - 10
					if vida <= 0:
						muerto = True
			else:
				coordX_bat2 = coordX_bat2 - 10
				if coordX_bat2 < 0:
					coordX_bat2 = 950
				coordenadas_bat2 = (coordX_bat2, coordY_bat2)

			# Colisión Zombie (Muere con puño y patada, patada alta no le hace daño)
			if pygame.sprite.collide_rect(ElLuchador, Zombie):
				if accion == 'puño':
					punio.play(0)
					puntuacion = puntuacion + 20
					coordX_zom = 950
					coordenadas_zom = (coordX_zom, coordY_zom)
				elif accion == 'patada':
					patada.play(0)
					puntuacion = puntuacion + 20
					coordX_zom = 950
					coordenadas_zom = (coordX_zom, coordY_zom)
				else:
					ouch.play(0)
					vida = vida - 10
					if vida <= 0:
						muerto = True
			else:
				coordX_zom = coordX_zom - 10
				if coordX_zom < 0:
					coordX_zom = 950
				coordenadas_zom = (coordX_zom, coordY_zom)

			# Colisión Esqueleto (Idem zombie)
			if pygame.sprite.collide_rect(ElLuchador, Esqueleto):
				if accion == 'puño':
					punio.play(0)
					muerte_esq.play(0)
					puntuacion = puntuacion + 20
					coordX_esq = 950
					coordenadas_esq = (coordX_esq, coordY_esq)
				elif accion == 'patada':
					patada.play(0)
					muerte_esq.play(0)
					puntuacion = puntuacion + 20
					coordX_esq = 950
					coordenadas_esq = (coordX_esq, coordY_esq)
				else:
					ouch.play(0)
					vida = vida - 10
					if vida <= 0:
						muerto = True
			else:
				coordX_esq = coordX_esq - 10
				if coordX_esq < 0:
					coordX_esq = 950
				coordenadas_esq = (coordX_esq, coordY_esq)

			if muerto:
				accion = 'muerto'
				ElLuchador.accion_terminada = False
				ElLuchador.anim = 0				# Ponemos a 0 para mostrar animación muerto bien

			reloj.tick(30)

		# Termina la partida
		if mensj:	# Ha llegado al final, no muere
			accion = 'quieto'
		ElLuchador.update(coordenadas_luchador, accion)

		for i, p in enumerate(mejores_puntuaciones):	# Insertar nueva mejor puntuación
			if puntuacion > p:
				mejores_puntuaciones.insert(i, puntuacion)
				mejores_puntuaciones.pop()
				puntuacion = 0

		for i, p in enumerate(mejores_puntuaciones):	# Textos mejores puntuaciones
			MejoresPunt[i] = Fuente.render(str(i+1) + ": " + str(p), 0, (0,255,0))

		# Poner en la ventana
		Ventana.blit(Fondo1, (0, 0))
		Ventana.blit(Fondo, (0, 0))
		Ventana.blit(GameOver1, (100, 50))
		Ventana.blit(GameOver2, (3, 100))
		Ventana.blit(MejoresP, (500, 50))
		for i, p in enumerate(mejores_puntuaciones):
			Ventana.blit(MejoresPunt[i], (650, 80 + 25 * i))
		if mensj:
			Ventana.blit(Mensaje, (5, 5))
		Ventana.blit(ElLuchador.image, ElLuchador.rect)

		pygame.display.flip()	# Mostrar

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:	# Salir cerrando la ventana
				sys.exit()

			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:	# Salir pusando ESC
					sys.exit()
				elif evento.key == pygame.K_r: 		# Reintentar
					muerto = False
					ElLuchador.accion_terminada = True

main()


