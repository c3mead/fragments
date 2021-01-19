import pygame, math, random
from pygame.sprite import Sprite

class Enemy(Sprite):
	"""Modeling enemy sprite movements."""
	
	def __init__(self, ai, var, screen, ship, call, y_loc):
		super().__init__()		
		"""Initialize enemy ships"""
		self.screen = screen
		self.ai = ai
		self.var = var
		self.call = call
		self.y_loc = y_loc
		
		self.image = var.b_ship[self.call]
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
				
		self.rect.left = self.screen_rect.right
		self.rect.centery = self.y_loc
		
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		
		self.osc = math.pi/2
		self.hits = 0
		
		self.start = pygame.time.get_ticks()
		self.start2 = pygame.time.get_ticks()
		self.fire_lag = 4000
		self.bullet_timer = self.start + self.fire_lag
		self.homing = 0
		self.spray = 0
		self.s_amount = 3
		
		self.dead = 0
		self.angle = 0
		self.dead_time = 0
		self.current = 0
		self.gone = 0
		self.hp = ai.e_hp[self.call]
		
		self.pattern = 0
		self.targetx = self.rect.x - 60
		self.target2 = 0
		self.quick_maffs = 1
		self.wait = 0
		self.fired = 0
		self.toggle = 1
		self.backwards = 0
		
		self.laser = 0
		self.boomed = 0
		self.t_boomed = 0
		
		self.t_x = -30
		self.y_y = 0
		self.x_x = 0
		self.m = 0
		self.b = 0
		self.t_y = 0
		
		self.laser_time = pygame.time.get_ticks()
		self.score = ai.e_score[self.call]
		
		self.chance = random.randint(0, 100)
		
	def update(self, ai):
		"""Models enemy ship movement."""
		
	def draw_enemy(self):
		"""Draw enemy ship."""
		self.screen.blit(self.image, self.rect)

#	def got_hit(self):
#		"""If player bullets hit enemy ship."""
#		self.hits += 1
		
	def boom(self):
		if self.boomed == 1:
			if self.t_boomed + 500 <= self.current:
				self.boomed = 0
		
	def defeat(self):
		"""Enemy ship gets shot down."""
		self.current = pygame.time.get_ticks()
		self.boomed = 1
		self.y += 1.07
		self.x -= 0.53
		self.angle += 0.01
		self.image = pygame.transform.rotate(self.image, self.angle)
		
		self.rect.x = self.x
		self.rect.y = self.y
		
		if (self.dead_time + 950) <= self.current:
			self.gone = 1
