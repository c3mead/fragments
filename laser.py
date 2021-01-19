import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
	"""Manage lasers fired from the ship."""
	
	def __init__(self, ai, screen, ship, enemy):
		super().__init__()
		"""Create lasers at ship location."""
		self.screen = screen
		self.ai = ai
		
		self.area = pygame.Surface((65, 34), pygame.SRCALPHA, 32)
		self.rect = self.area.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.centery = ship.rect.centery
		self.area.fill((0, 0, 0, 0))
		
		self.color_1 = ai.b4_color
		self.color_2 = ai.b5_color
		self.thick_1 = 2
		self.thick_2 = 6
				
		self.t_x = -30
		self.t_y = -100
		self.gone = 0
		self.start = pygame.time.get_ticks()
		self.hurt = 0
		self.damage = 0.4
		
		self.y_y = enemy.rect.centery - ship.rect.centery
		self.x_x = enemy.rect.centerx - ship.rect.centerx
		self.m = float(self.y_y / self.x_x)
		self.b = enemy.rect.centery - (self.m * enemy.rect.centerx)
		self.t_y = (self.m * self.t_x) + self.b
		
		self.e_x = enemy.rect.centerx
		self.e_y = enemy.rect.centery
			
	def draw_laser(self):
		self.current = pygame.time.get_ticks()
		if self.start + 750 >= self.current:
			pygame.draw.line(self.screen, self.color_1, (self.t_x, self.t_y), 
				(self.e_x, self.e_y), self.thick_1)
		elif self.start + 1050 >= self.current:
			pygame.draw.line(self.screen, self.color_1, (-100, -100), 
				(-200, -200), self.thick_1)
		elif self.start + 1950 >= self.current:
			self.hurt = 1
			self.screen.blit(self.area, self.rect)
			pygame.draw.line(self.screen, self.color_2, (self.t_x, self.t_y), 
				(self.e_x, self.e_y), self.thick_2)
		else:
			self.gone = 1
