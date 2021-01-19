import pygame
import pygame.font

class Hub():
	"""Borders, Health display, Special, and score display."""
	
	def __init__(self, ai, var, screen):
		self.screen = screen
		self.ai = ai
		self.var = var
		
		# Card
		self.card = pygame.image.load('images/hub/p_claude.png')
		self.card = pygame.transform.scale2x(self.card)
		self.c_rect = self.card.get_rect()
		self.c_rect.bottom = ai.height - 12
		self.c_rect.centerx = ai.width/2
		
		# Initialize health
		self.h_bar = float(100)
		self.h_shade_1 = (160, 248, 104)
		self.h_shade_2 = (72, 216, 0)
		self.h_shade_3 = (64, 136, 32)
		self.h_y = self.c_rect.bottom - 72
		
		# Initialize shield
		self.s_bar = float(100)
		self.s_shade_1 = (247, 238, 54)
		self.s_shade_2 = (247, 177, 0)
		self.s_shade_3 = (247, 85, 0)
		self.s_y = self.h_y + 24
		
		# Score font
		self.score = 0
		self.s_color = (255, 255, 255)
		self.s_font = pygame.font.SysFont(None, 28)
		
		self.pause = 1		
		self.chapter = 0
		self.current = 0
		self.death = 0
		self.timed = 0
		
#		self.init = 0
#		self.start = 1
#		self.inputs = 1
#		self.backgrounds = 1
#		self.bullets = 1
#		self.lasers = 1
#		self.ship = 1
#		self.enemy = 1
#		self.hub = 1
		
		# Skip Title Scren
		self.init = 1
		self.start = 0
		self.inputs = 0
		self.backgrounds = 0
		self.bullets = 0
		self.lasers = 0
		self.ship = 0
		self.enemy = 0
		self.hub = 0
		
	def update(self, ai):
		# Limits
		if self.h_bar <= 0:
			self.h_bar = 0
		elif self.h_bar >= 100:
			self.h_bar = 100
			
		if self.s_bar <= 0:
			self.s_bar = 0
		elif self.s_bar >= 100:
			self.s_bar = 100
		
		# black borders
		pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, ai.width, (116)))
		pygame.draw.rect(self.screen, (0, 0, 0), (0, ((ai.height-116)), ai.width, (116)))	
		# Card
		self.screen.blit(self.card, self.c_rect)	
		# health bar
		pygame.draw.rect(self.screen, self.h_shade_1, ((self.c_rect.left + 90), (self.h_y), (self.h_bar), 2))
		pygame.draw.rect(self.screen, self.h_shade_2, ((self.c_rect.left + 90), (self.h_y + 2), (self.h_bar), 1))
		pygame.draw.rect(self.screen, self.h_shade_3, ((self.c_rect.left + 90), (self.h_y + 3), (self.h_bar), 1))
		# shield bar
		pygame.draw.rect(self.screen, self.s_shade_1, ((self.c_rect.left + 90), (self.s_y), (self.s_bar), 2))
		pygame.draw.rect(self.screen, self.s_shade_2, ((self.c_rect.left + 90), (self.s_y + 2), (self.s_bar), 1))
		pygame.draw.rect(self.screen, self.s_shade_3, ((self.c_rect.left + 90), (self.s_y + 3), (self.s_bar), 1))
		
		# Score
		self.s_str = str(self.score)
		self.s_img = self.s_font.render(self.s_str, True, self.s_color, (0, 0, 0))
		self.s_rect = self.s_img.get_rect()
		self.s_rect.right = 23 * ai.width / 24
		self.s_rect.centery = ai.height / 24
		self.screen.blit(self.s_img, self.s_rect)
		
	def halt(self):
		"""Pauses all processes."""
		self.inputs *= -1
		self.backgrounds *= -1
		self.bullets *= -1
		self.lasers *= -1
		self.ship *= -1
		self.enemy *= -1
		
	def za_wurado(self, ai):
		self.bullets = 1
		self.lasers = 1
		self.enemy = 1
		ai.static_speed = 0
		ai.static_speed = 0

