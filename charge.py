import pygame
from pygame.sprite import Sprite

class Charge(Sprite):
	
	def __init__(self, ai, var, screen, ship):
		super().__init__()
		"""Charge shot graphics."""
		self.screen = screen
		self.ai = ai
		self.var = var
		
		self.frames = var.charge2
		self.fulls = var.charge
		self.image = var.charge[0]
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = ship.rect.right 
		self.rect.centery = ship.rect.centery 
		
		self.y = float(self.rect.centery)
		self.x = float(self.rect.centerx)
		
		self.effect_level = 0
		self.lag = 75
		
		self.start = pygame.time.get_ticks()
		self.start2 = pygame.time.get_ticks()

		self.charge_level = 0
		self.charge_level2 = 0

		self.current = 0
		
	def charge(self, screen, ship):
		self.x = ship.rect.right
		self.y = ship.rect.centery
		self.rect.centerx = self.x
		self.rect.centery = self.y
		
		self.current = pygame.time.get_ticks()
		if (self.start + self.lag) <= self.current:
			if self.effect_level < 5:
				self.effect_level += 1
				self.start = pygame.time.get_ticks()
			else:
				self.effect_level = 0
		
		if self.charge_level == 2:
			self.lag = 45
			self.full = self.fulls[self.effect_level]
			self.full = pygame.transform.scale2x(self.full)
			self.full.set_colorkey((128, 255, 255))
			self.screen.blit(self.full, self.rect)
			
		elif self.charge_level == 1:
			self.lag = 75
			self.frame = self.frames[self.effect_level]
			self.frame = pygame.transform.scale2x(self.frame)
			self.frame.set_colorkey((255, 128, 255))
			self.screen.blit(self.frame, self.rect)
