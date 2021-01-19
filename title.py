import pygame, sys

class Title():
	"""Title Screen Shenanigans."""
	
	def __init__(self, ai, var, screen, hub):
		self.ai = ai
		self.screen = screen
		self.var = var
		
		self.back_1 = pygame.image.load('images/backgrounds/c0_lushkia.png').convert()
		self.back_1 = pygame.transform.scale(self.back_1, (642, 360))
		self.back_1.set_colorkey((255, 0, 0))
		self.back_1.set_alpha(150)

		self.logo = pygame.image.load('images/backgrounds/c0_title.png').convert()
		self.logo.set_colorkey((255, 0, 0))
		self.logo.set_alpha(175)
		
		self.t_blocks = var.title
		self.t_block = self.t_blocks[0]
		self.t_block = pygame.transform.scale(self.t_block, (185, 138))
		
		self.choice = pygame.image.load('images/hub/t_choice_2.png')
		self.choice = pygame.transform.scale(self.choice, (185, 138))

		# Positioning Backgrounds
		self.screen_rect = self.screen.get_rect()

		self.pos1 = self.back_1.get_rect()
		self.pos2 = self.logo.get_rect()
		
		self.pos1.top = self.screen_rect.top + 75
		self.pos1.centerx = self.screen_rect.centerx
	
		self.pos2.top = self.screen_rect.top + 200
		self.pos2.centerx = self.screen_rect.centerx
	
		self.pos3 = self.pos4 = self.t_block.get_rect()
		self.pos3.centery = self.pos4.centery = (ai.height/2) + 150
		self.pos3.centerx = self.pos4.centerx = ai.width/2
			
		self.current = 0
		self.timer = 0
		self.screen = 0
		self.select = 1
		self.enter = 0
		self.alpha = 0

		self.fade = pygame.Surface((ai.width, ai.height))
		self.fade.fill((255,255,255))
		
		self.chapters = var.chapters
		self.chapter = self.chapters[hub.chapter]
		self.chapter = pygame.transform.scale(self.chapter, (ai.width, ai.height))
