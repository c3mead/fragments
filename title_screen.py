import pygame, sys, math
import pygame.font
from ship import Ship

import game_functions as gf

def title_screen(ai, var, screen, ship, statics, backgrounds, hub, title):
	title.current = pygame.time.get_ticks()

	if title.enter == 0 or title.enter == 1:
		#Background
		#gf.loop_background(ai, var, screen, statics, backgrounds)
		screen.fill((0, 0, 0))
	
		# Graphics
		#title.back_1.fill((255, 0, 255))
		screen.blit(title.back_1, title.pos1)
	
		# Select
		title.t_block = title.t_blocks[(title.select-1)]
		title.t_block = pygame.transform.scale(title.t_block, (185, 138))
		screen.blit(title.t_block, title.pos3)
		screen.blit(title.choice, title.pos4)
		
		# Borders
		pygame.draw.rect(screen, (0, 0, 0), (0, 0, ai.width, (ai.height/12)))
		pygame.draw.rect(screen, (0, 0, 0), (0, (11*(ai.height/12)), ai.width, (ai.height/12)))
			
		# Key Inputs
		if not title.enter:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						title.enter = 1
						title.timer = pygame.time.get_ticks()
					elif event.key == pygame.K_q:
						sys.exit()	
					elif event.key == pygame.K_DOWN:
						if title.select == 3:
							title.select = 3
						else:
							title.select += 1
					elif event.key == pygame.K_UP:
						if title.select == 1:
							title.select = 1
						else:
							title.select -=1
				
		elif title.enter == 1:
#			pygame.mixer.fadeout(3000)
			title.fade.set_alpha(title.alpha)
			screen.blit(title.fade, (0,0))
			if title.timer + 15 <= title.current:
				if title.alpha >= 255:
					title.enter = 2
					title.timer = pygame.time.get_ticks()
					title.alpha = 0
				else:
					title.alpha += 5
					title.timer = pygame.time.get_ticks()
	
	if title.enter == 2:
		screen.fill((255, 255, 255))
		title.chapter.set_alpha(title.alpha)
		screen.blit(title.chapter, (0,0))
		if title.timer + 10 <= title.current:
			if title.alpha >= 255:
				hub.init = 1
				hub.ship = 0
				hub.backgrounds = 0
				hub.hub = 0
				title.enter = 3
				title.timer = pygame.time.get_ticks()
				title.alpha = 255
			else:
				title.alpha += 5
				title.timer = pygame.time.get_ticks()
				
	if title.enter == 3:
		title.chapter.set_alpha(title.alpha)
		screen.blit(title.chapter, (0,0))
		if title.timer + 10 <= title.current:
			if title.alpha <= 0:
				hub.inputs = 0
				hub.bullets = 0
				hub.lasers = 0
				hub.enemy = 0
				hub.start = 0
			else:
				title.alpha -= 15
				title.timer = pygame.time.get_ticks()
