import pygame, sys, math
from pygame.sprite import Sprite

class Shock(Sprite):
	"""Manage explosions."""
	
	def __init__(self, ai, var, screen, enemy):
		super().__init__()
		self.screen = screen
		self.ai = ai
		self.var = var
		
		self.frames = var.explosion
		self.image = var.explosion[0]

	
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = enemy.rect.centerx 
		self.rect.centery = enemy.rect.centery 
		
		self.y = float(self.rect.centery)
		self.x = float(self.rect.centerx)
		self.effect_level = 0
		
		self.start = pygame.time.get_ticks()
		self.lag = 50
		self.gone = 0

	def explode(self, screen, enemy):
		self.frame = self.frames[self.effect_level]
		self.frame.set_colorkey((255, 255, 255))
		self.x = enemy.rect.centerx
		self.y = enemy.rect.centery
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self.current = pygame.time.get_ticks()
		if (self.start + self.lag) <= self.current:
			if self.effect_level < 9:
				self.effect_level += 1
				self.start = pygame.time.get_ticks()
			else:
				self.gone = 1
		self.screen.blit(self.frame, self.rect)

