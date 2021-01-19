import pygame
from pygame.sprite import Sprite

class Slay(Sprite):
	"""Manage bullets fired from the ship."""
	
	def __init__(self, ai, screen, ship, enemy, _type, slope):
		"""Create bullets at ship location."""
		super().__init__()
		self.screen = screen
		self.ai = ai
		self.type = _type
		self.slope = float(slope/6)
		
		self.rect = pygame.Rect(0, 0, ai.b1_width, ai.b1_height)
		self.rect.centerx = enemy.rect.centerx
		self.rect.centery = enemy.rect.centery
		self.position = (self.rect.centerx, self.rect.centery)
		
		# May need to create a small surface then draw bullets onto surface
		# in order to create a mask
		
		if self.type == 1:
			self.damage = 10
		if self.type == 2:
			self.damage = 3
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		self.color = ai.b1_color
		self.color2 = ai.b2_color
		self.speed = ai.b1_speed
		self.radius = 10
		self.radius2 = 6
				
		# y = mx + b
		self.y_y = enemy.rect.centery - ship.rect.centery
		self.x_x = enemy.rect.centerx - ship.rect.centerx
		self.m = float(self.y_y / self.x_x)
		self.b = enemy.rect.centery - (self.m * enemy.rect.centerx)
		self.e_x = enemy.rect.centerx
		self.e_y = enemy.rect.centery

	def update(self):
		self.x -= 1
		# Homing
		if self.type == 1:
			self.y = (self.m * self.x) + self.b
		#Spray
		elif self.type == 2:
			if not self.slope == 0:
				self.b = self.e_y - (self.slope * self.e_x)
				self.y = (self.slope * self.x) + self.b
				
		self.rect.x = self.x
		self.rect.y = self.y
		self.position = (self.rect.centerx, self.rect.centery)
		
	def draw_shot(self):
		if self.type == 1:
			pygame.draw.circle(self.screen, self.color, self.position, self.radius)
		elif self.type == 2:
			pygame.draw.circle(self.screen, self.color2, self.position, self.radius2)
