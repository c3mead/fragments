import pygame
from pygame.sprite import Sprite

class Background(Sprite):
	"""Moving background."""
	
	def __init__(self, ai, var, screen):
		"""Initialize the background."""
		super().__init__()		
		self.screen = screen
		self.ai = ai
		self.vars = var
		
		# Load background and get its rect
		self.frames = var.o_back
		self.image = var.o_back[ai.back]		
		self.image = pygame.transform.scale(self.image, (ai.width, ai.height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Position the background
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		# Store background's exact location
		self.x = float(self.rect.x)
		
		self.back = ai.back
		
	def update(self):
		"""Background image travel."""
		self.x -= self.ai.background_speed
		self.rect.x = self.x
