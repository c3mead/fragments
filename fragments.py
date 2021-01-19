#Fragments

import pygame

from settings import Settings
from ship import Ship
from variance import Variance
from wave import Wave
from hub import Hub
from title import Title

from pygame.sprite import Group

import title_screen as ts
import game_functions as gf
import enemy_movements as em

def run_game():
	pygame.init()
	ai = Settings()
	var = Variance()
	wave = Wave(ai, var)
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((ai.width, ai.height))
	hub = Hub(ai, var, screen)
	pygame.display.set_caption("Fragments")

	pygame.mixer.init()
	pygame.mixer.music.load('music/3.mp3')
	pygame.mixer.music.play(-1)
	
	bg_color = (150, 150, 150)
	
	statics = Group()
	backgrounds = Group()
	enemies = Group()
	shots = Group()
	slayers = Group()
	shockers = Group()
	charges = Group()
	shields = Group()
	blasters = Group()
	lasers = Group()
	items = Group()
	deaths = Group()
	ship = 'poop'

	title = Title(ai, var, screen, hub)

	while True:
		if hub.init == 1:
			ship = Ship(ai, var, screen)
			gf.set_background(ai, var, screen, statics, backgrounds)
			hub.init = 2
			
		if hub.inputs == 0:
			gf.check_events(ai, var, screen, ship, shots, enemies, charges, shields, blasters, hub)
			
		if hub.backgrounds == 0:
			gf.loop_background(ai, var, screen, statics, backgrounds)
			
		if hub.bullets == 0:
			gf.bullet_updates(ai, var, screen, ship, enemies, shots, 
				blasters, slayers, lasers, shockers, charges, shields, items, hub)
				
		if hub.lasers == 0:
			gf.laser_updates(ai, screen, ship, enemies, lasers)
			
		if hub.ship == 0:
			gf.ship_updates(ai, var, screen, ship, charges, shields, hub)
			
		if hub.enemy == 0:
			gf.enemy_update(ai, var, screen, ship, enemies, slayers, 
				shockers, lasers, wave, hub)
				
		if hub.hub == 0:
			gf.update_hub(ai, var, screen, ship, hub, deaths)
			
		if hub.start:
			ts.title_screen(ai, var, screen, ship, statics, backgrounds, hub, title)
			
		gf.menu_screen(ai, screen, statics, backgrounds, ship, 
			enemies, shots, slayers, hub)
			
		pygame.display.flip()
		
run_game()
