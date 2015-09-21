#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class UndeadKing(pygame.sprite.Sprite):

	def __init__(self, coordenadas):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = pygame.image.load("img/undeadking.png")
		self.arrayAndar = []
		self.anim = 0
		self.actualizado = pygame.time.get_ticks()

		a = 0
		while a < 3:
			self.arrayAndar.append(self.ImgCompleta.subsurface((a * 64, 295, 64, 90)))
			a = a + 1

		self.image = self.arrayAndar[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas

	def update(self, nuevas_coordenadas):

		self.rect.center = nuevas_coordenadas
		if self.actualizado + 100 < pygame.time.get_ticks():
			self.anim = self.anim + 1
			if self.anim > 2:
				self.anim = 0
			self.image = self.arrayAndar[self.anim]
			self.actualizado = pygame.time.get_ticks()


class Bat(pygame.sprite.Sprite):

	def __init__(self, coordenadas, tipo):	# tipo: En la imagen completa hay dos murciélagos, tipo indica cuál escoger
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = pygame.image.load("img/bat.png")
		self.arrayAndar = []
		self.anim = 0
		self.actualizado = pygame.time.get_ticks()

		if tipo == 1:		# Murciélago negro
			altura = 0
		else:				# Murciélago marrón
			altura = 64

		a = 0
		while a < 5:
			self.arrayAndar.append(self.ImgCompleta.subsurface((a * 64, altura, 64, 64)))
			a = a + 1

		self.image = self.arrayAndar[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas

	def update(self, nuevas_coordenadas):

		self.rect.center = nuevas_coordenadas
		if self.actualizado + 100 < pygame.time.get_ticks():
			self.anim = self.anim + 1
			if self.anim > 4:
				self.anim = 0
			self.image = self.arrayAndar[self.anim]
			self.actualizado = pygame.time.get_ticks()


class Zombiesqueleto(pygame.sprite.Sprite):

	def __init__(self, coordenadas, tipo):	# tipo: Hay un zombie y un esqueleto en la imagen completa
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = pygame.image.load("img/zombie_n_skeleton.png")
		self.tipo = tipo
		self.arrayAndar = []
		self.anim = 0
		self.actualizado = pygame.time.get_ticks()

		if tipo == 1:			# Zombie
			ancho_extra = 0
		else:					# Esqueleto
			ancho_extra = 195

		a = 0
		while a < 3:
			self.arrayAndar.append(self.ImgCompleta.subsurface((ancho_extra + a * 65, 155, 65, 100)))	
			a = a + 1

		self.image = self.arrayAndar[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas

	def update(self, nuevas_coordenadas):

		self.rect.center = nuevas_coordenadas
		if self.actualizado + 100 < pygame.time.get_ticks():
			self.anim = self.anim + 1
			if self.anim > 2:
				self.anim = 0
			self.image = self.arrayAndar[self.anim]
			self.actualizado = pygame.time.get_ticks()


