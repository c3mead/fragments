import pygame
from pygame.sprite import Sprite

class Shot(Sprite):
	"""Manage bullets fired from the ship."""
	
	def __init__(self, ai, screen, ship, num):
		"""Create bullets at ship location."""
		super().__init__()
		self.screen = screen
		self.ai = ai
		self.num = num
		
		self.rect = pygame.Rect(0, 0, ai.b1_width, ai.b1_height)
		self.rect.left = ship.rect.centerx
		if self.num == 1:
			self.rect.centery = ship.rect.centery
		elif self.num == 2:		
			self.rect.centery = ship.rect.centery - 5
		elif self.num == 3:
			self.rect.centery = ship.rect.centery + 5
			
		self.x = float(self.rect.x)
		
		self.color = ai.b3_color
		self.speed = ai.b1_speed
		
	def update(self):
		"""Move across screen."""
		self.x += self.speed
		self.rect.x = self.x
		
	def draw_shot(self):
		pygame.draw.ellipse(self.screen, self.color, self.rect)
