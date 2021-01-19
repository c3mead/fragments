import pygame, sys, math
from pygame.sprite import Sprite

class Death(Sprite):
	"""Manage explosions."""
	
	def __init__(self, ai, var, screen, ship):
		super().__init__()
		self.screen = screen
		self.ai = ai
		self.var = var
		
		self.frames = var.death
		self.image = var.death[0]
	
		self.rect = self.image.get_rect()

		self.rect.centerx = ship.rect.centerx 
		self.rect.centery = ship.rect.centery 
		
		self.y = float(self.rect.centery)
		self.x = float(self.rect.centerx)
		self.effect_level = 0
		
		self.start = pygame.time.get_ticks()
		self.lag = 50
		self.gone = 0

	def death(self):
		self.image = self.frames[self.effect_level]
		self.image.set_colorkey((0, 0, 0))
		
		self.current = pygame.time.get_ticks()
		if (self.start + self.lag) <= self.current:
			if self.effect_level < 7:
				self.effect_level += 1
				self.start = pygame.time.get_ticks()
			else:
				self.gone = 1
		self.screen.blit(self.image, self.rect)

