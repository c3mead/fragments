import pygame
from pygame.sprite import Sprite
# 0, 128, 128

class Blast(Sprite):
	"""Class modeling the charged shots."""
	
	def __init__(self, ai, var, screen, ship):
		super().__init__()
		self.screen = screen
		self.ai = ai
		self.var = var
		
		self.frames = var.buster
		self.image = var.buster[0]
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = ship.rect.right 
		self.rect.centery = ship.rect.centery 
		
		self.y = float(self.rect.centery)
		self.x = float(self.rect.centerx)
		
		self.effect_level = -1
		self.lag = 40
		self.speed = 11
		
		self.start = pygame.time.get_ticks()
		self.current = 0

	def boom(self):
		"""Bullet movement."""
		self.x += self.speed
		self.rect.centerx = self.x
		
		self.current = pygame.time.get_ticks()
		if (self.start + self.lag) <= self.current:
			if self.effect_level < 3:
				self.effect_level += 1
				self.start = pygame.time.get_ticks()
			else:
				self.effect_level = 0

		self.frame = self.frames[self.effect_level]
		self.frame = pygame.transform.scale2x(self.frame)
		self.frame.set_colorkey((0, 128, 128))
		self.screen.blit(self.frame, self.rect)
