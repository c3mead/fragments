import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
	
	def __init__(self, ai, var, screen, ship, hub):
		super().__init__()
		self.ai = ai
		self.var = var
		self.screen = screen
		
		# Shield Graphics
		self.frames = [1, 2, 3, 4, 5, 6, 7]
		self.frames[0] = pygame.image.load('images/effects/shield/k_b1.png').convert()
		self.frames[1] = pygame.image.load('images/effects/shield/k_b2.png').convert()
		self.frames[2] = pygame.image.load('images/effects/shield/k_b3.png').convert()
		self.frames[3] = pygame.image.load('images/effects/shield/k_b4.png').convert()
		self.frames[4] = pygame.image.load('images/effects/shield/k_b5.png').convert()
		self.frames[5] = pygame.image.load('images/effects/shield/k_b6.png').convert()
		self.frames[6] = pygame.image.load('images/effects/shield/k_b7.png').convert()
		
		self.area = pygame.Surface((72, 38), pygame.SRCALPHA, 32)
		self.area.fill((0, 0, 0, 0))
		
		#self.frames = var.shield
		self.image = self.frames[0]
		#self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = ship.rect.right 
		self.rect.centery = ship.rect.centery 
		
		self.y = float(self.rect.centery)
		self.x = float(self.rect.centerx)
		
		self.effect_level = 0
		self.lag = 15
		self.red = (255, 0, 0)
		
		self.start = self.time_bar = pygame.time.get_ticks()
		self.charge_level = 0
		self.current = 0
		self.pos = 0
		self.rad = 42

	def shield(self, screen, ship, hub):
		self.area = pygame.Surface((72, 38), pygame.SRCALPHA, 32)
		self.area.fill((0, 0, 0, 0))
		self.x = ship.rect.centerx
		self.y = ship.rect.centery
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self.pos = (self.x, self.y)
		
		self.current = pygame.time.get_ticks()
		if (self.start + self.lag) <= self.current:
			if self.effect_level < 6:
				self.effect_level += 1
				self.start = pygame.time.get_ticks()
			else:
				self.effect_level = 0
				
		if self.time_bar + 25 <= self.current:
			if hub.s_bar >= 1:
				hub.s_bar -= 1
				self.time_bar = pygame.time.get_ticks()
			
		self.image = self.frames[self.effect_level]
		self.image.set_colorkey(self.red)
		self.image.set_alpha(200)
		pygame.draw.circle(self.area, (0, 0, 0, 0), (36, 19), self.rad)
		self.screen.blit(self.area, (ship.rect.top, ship.rect.left))
		self.screen.blit(self.image, self.rect)
