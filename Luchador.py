#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Luchador(pygame.sprite.Sprite):

	def __init__(self, coordenadas):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = pygame.image.load("img/kung-fu.png")
		self.accion_terminada = True
		self.imgQuieto = self.ImgCompleta.subsurface((35, 0, 55, 90)) # minx, miny, maxx-minx, maxy-miny
		self.arrayCorrer = []
		self.arrayPunio = []
		self.arrayPatada = []
		self.arrayPatadaAlta = []
		self.arrayMuerte = []

		# Recoger sprites
		a = 0				# Correr
		while a < 6:
			self.arrayCorrer.append(self.ImgCompleta.subsurface((a * 88, 120, 88, 87)))
			a = a + 1

		a = 0				# Puñetazo
		while a < 4:
			self.arrayPunio.append(self.ImgCompleta.subsurface((a * 82, 235, 82, 90)))
			a = a + 1

		a = 0				# Patada
		while a < 4:
			self.arrayPatada.append(self.ImgCompleta.subsurface((474 + a*87, 230, 87, 90)))
			a = a + 1

		a = 0				# Patada alta
		while a < 4:
			self.arrayPatadaAlta.append(self.ImgCompleta.subsurface((474 + a*87, 330, 87, 90)))
			a = a + 1

		a = 0				# Muerte
		while a < 8:
			self.arrayMuerte.append(self.ImgCompleta.subsurface((a * 58, 340, 58, 90)))
			a = a + 1

		self.anim = 0
		self.actualizado = pygame.time.get_ticks()
		self.image = self.imgQuieto
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas


	def update(self, nuevas_coordenadas, accion):

		if accion == 'correr':						# Correr
			self.rect.center = nuevas_coordenadas
			if self.actualizado + 100 < pygame.time.get_ticks():
				self.anim = self.anim + 1
				if self.anim > 5:
					self.anim = 0
				self.image = self.arrayCorrer[self.anim]
				self.actualizado = pygame.time.get_ticks()

		elif accion == 'puño':						# Puñetazo
			if self.actualizado + 100 < pygame.time.get_ticks():
				if self.anim < 3:
					self.anim = self.anim + 1
					self.image = self.arrayPunio[self.anim]
				else:
					self.accion_terminada = True		# Los ataques bloquean al luchador hasta que termine el golpe
					self.image = self.imgQuieto
				self.actualizado = pygame.time.get_ticks()

		elif accion == 'patada':					# Patada
			if self.actualizado + 100 < pygame.time.get_ticks():
				if self.anim < 3:
					self.anim = self.anim + 1
					self.image = self.arrayPatada[self.anim]
				else:
					self.accion_terminada = True
					self.image = self.imgQuieto
				self.actualizado = pygame.time.get_ticks()

		elif accion == 'patada_alta':				# Patada alta
			if self.actualizado + 100 < pygame.time.get_ticks():
				if self.anim < 3:
					self.anim = self.anim + 1
					self.image = self.arrayPatadaAlta[self.anim]
				else:
					self.accion_terminada = True
					self.image = self.imgQuieto
				self.actualizado = pygame.time.get_ticks()

		elif accion == 'muerto':					# Muerte
			if self.actualizado + 100 < pygame.time.get_ticks():
				if self.anim < 7:
					self.anim = self.anim + 1
				else:
					self.accion_terminada = True
				self.image = self.arrayMuerte[self.anim]
				self.actualizado = pygame.time.get_ticks()

		else:										# Quieto
			self.image = self.imgQuieto


