import pygame

class Ship():
	
	def __init__ (self, ai, var, screen):
		"""Initialize ship and its starting position."""
		self.screen = screen
		self.ai = ai
		self.var = var
		
		self.frames = var.p_ship
		self.image = self.frames[0]
		self.image = pygame.transform.scale(self.image, (72, 38))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		
		self.rect.left = self.screen_rect.left + (ai.width/9)
		self.rect.centery = self.screen_rect.centery
		
		self.center_y = float(self.rect.centery)
		self.center_x = float(self.rect.centerx)

		self.s_count = 1
		self.charge = 0
		self.shield = 0
		self.move_down = 0
		self.move_up = 0

	def update(self, ai):
		"""Update the ship's posiiton and shape."""
		if self.move_up and self.rect.top > (116):
			self.image = self.frames[1]
			self.image = pygame.transform.scale(self.image, (72, 38))
			self.center_y -= self.ai.speed_ratio
		elif self.move_down and self.rect.bottom <= ((ai.height-116)):
			self.image = self.frames[2]
			self.image = pygame.transform.scale(self.image, (72, 38))
			self.center_y += self.ai.speed_ratio
		else:
			self.image = self.frames[0]
			self.image = pygame.transform.scale(self.image, (72, 38))
		
		self.mask = pygame.mask.from_surface(self.image)
				
		self.rect.centery = self.center_y
		self.rect.centerx = self.center_x

	def draw_ship(self):
		"""Draw the background."""
		self.screen.blit(self.image, self.rect)
		
	def damage(self):
		"""Ship takes damage."""
		print('Check')
