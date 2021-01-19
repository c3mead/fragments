import pygame
from pygame.sprite import Sprite

class Item(Sprite):
	
	def __init__(self, ai, var, screen, enemy, hub, type_):
		super().__init__()
		self.ai = ai
		self.var = var
		self.screen = screen
		self.type = type_
		
		if self.type == 1:
			self.images = var.health
			self.f_max = 7
			self.plus = 20
		elif self.type == 2:
			self.images = var.ability
			self.f_max = 2
			self.plus = 10
			
		self.image = self.images[0]
		self.image.set_colorkey((0, 162, 232))
		self.rect = self.image.get_rect()
		self.rect.centerx = enemy.rect.centerx
		self.rect.centery = enemy.rect.centery
		
		self.x = float(self.rect.x)
		
		self.delay = 85
		self.start = pygame.time.get_ticks()
		self.current = 0
		self.frame = 0
		
	def update(self):		
		self.current = pygame.time.get_ticks()
		self.x -= 0.75
		
		if self.start + self.delay <= self.current:
			self.start = pygame.time.get_ticks()
			if self.frame == self.f_max:
				self.frame = 0
			else:
				self.frame += 1
				
		self.image = self.images[self.frame]
		self.image.set_colorkey((0, 162, 232))
		self.rect.x = self.x
		self.screen.blit(self.image, self.rect)
