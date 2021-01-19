import pygame, sys, math
import pygame.font
from settings import Settings
from slay import Slay
from laser import Laser

import game_functions as gf

# Enemy attack patterns.

def load_movement(ai, var, screen, ship, enemy, slayers, lasers):
	"""Animation when enemy arrives."""
	if enemy.call == 0:
		enemy.targetx = ai.width * (8/10)
		enemy_one(ai, var, screen, ship, enemy, slayers)
	elif enemy.call == 1:
		enemy_two(ai, var, screen, ship, enemy, slayers)
	elif enemy.call == 2:
		enemy_three(ai, var, screen, ship, enemy, slayers)
	elif enemy.call == 3:
		enemy.targetx = ai.width * (7/10)
		enemy_four(ai, var, screen, ship, enemy, slayers, lasers)
	elif enemy.call == 4:
		enemy.targetx = ai.width * (6.5/10)
		enemy.target2x = ai.width + 20
		enemy_five(ai, var, screen, ship, enemy, slayers, lasers)
		
def enemy_one(ai, var, screen, ship, enemy, slayers):
	"""Big Ship pans to spot and floats while firing patterned bullets."""
	if not enemy.pattern:
		enemy.x -= 1.35
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		if enemy.targetx >= enemy.x:
			enemy.pattern = 1
			enemy.start = pygame.time.get_ticks()
	if enemy.pattern:
		enemy.current = pygame.time.get_ticks()
		enemy.osc += (math.pi / 512)
		enemy.y += ((math.sin(enemy.osc)) / 6)
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		if enemy.start + 1000 <= enemy.current:
			enemy.spray = 1
			enemy.s_amount = 3
			add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
			enemy.start = pygame.time.get_ticks()
			
def enemy_two(ai, var, screen, ship, enemy, slayers):
	"""Small-ish ship that moves closer after every shot."""
	if enemy.wait == 0:
		enemy.targety = ship.rect.y
		enemy.x -= 4
		enemy.y += (6 * (enemy.quick_maffs / abs(enemy.quick_maffs)))
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		if enemy.x <= enemy.targetx:
			enemy.wait = 1
			enemy.start = pygame.time.get_ticks()
		
	elif enemy.wait == 1:
		enemy.current = pygame.time.get_ticks()
		if enemy.start + 1000 <= enemy.current:	
			if enemy.fired == 0:
				enemy.homing = 1
				add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
				enemy.fired = 1
		if enemy.start + 2000 <= enemy.current:	
			enemy.start = pygame.time.get_ticks()
			enemy.wait = 0
			enemy.fired = 0
			enemy.quick_maffs = (ship.rect.y - enemy.rect.y)
			if enemy.quick_maffs == 0:
				enemy.quick_maffs = 1
			enemy.targetx = enemy.rect.x - 60

def enemy_three(ai, var, screen, ship, enemy, slayers):
	""""Miniture ship that just runs from right to left."""
	enemy.current = pygame.time.get_ticks()
	enemy.x -= 3
	enemy.rect.y = enemy.y
	enemy.rect.x = enemy.x
	if not enemy.fired:
		if enemy.start + 1000 <= enemy.current:
			enemy.homing = 1
			add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
			enemy.start = pygame.time.get_ticks()
	
def enemy_four(ai, var, screen, ship, enemy, slayers, lasers):
	"""BIG BOSS DADDY SHIP."""
	if not enemy.pattern:
		enemy.x -= 0.50
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		if enemy.targetx >= enemy.x:
			enemy.pattern = 1
			enemy.laser_time = pygame.time.get_ticks()
			enemy.start = pygame.time.get_ticks()
			enemy.start2 = pygame.time.get_ticks()
			
	if enemy.pattern:
		enemy.current = pygame.time.get_ticks()
		
		# Laser
		if enemy.laser == 0:
			if enemy.laser_time + 4000 <= enemy.current:
				enemy.laser = 1
				enemy.laser_time = pygame.time.get_ticks()
		elif enemy.laser == 1:
			if enemy.laser_time + 2500 <= enemy.current:
				add_enemy_laser(ai, screen, ship, enemy, lasers)
				enemy.laser = 2
				enemy.laser_time = pygame.time.get_ticks()
		elif enemy.laser == 2:
			if enemy.laser_time + 2200 <= enemy.current:
				enemy.laser = 0
				enemy.laser_time = pygame.time.get_ticks()
		
		# Movement
		enemy.osc += (math.pi / 512)
		enemy.y += ((math.sin(enemy.osc)) / 6)
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		
		# Spray Bullets
		if enemy.start + 750 <= enemy.current:
			enemy.homing = 0
			enemy.spray = 1
			enemy.s_amount = 5
			add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
			enemy.start = pygame.time.get_ticks()
			
		# Homing Bullets
		if enemy.start2 + 1250 <= enemy.current:
			enemy.homing = 1
			enemy.spray = 0
			add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
			enemy.start2 = pygame.time.get_ticks()
				
def enemy_five(ai, var, screen, ship, enemy, slayers, lasers):
	"""Moves into screen, fires bullets, retreats, then repeats."""
	if not enemy.pattern:
		enemy.x -= (3.5 * enemy.toggle)
		enemy.rect.y = enemy.y
		enemy.rect.x = enemy.x
		if enemy.targetx >= enemy.x:
			enemy.pattern = 1
			enemy.start = pygame.time.get_ticks()
			enemy.laser_time = pygame.time.get_ticks()
			
	if enemy.pattern:
		enemy.current = pygame.time.get_ticks()
	
		# Laser
		if enemy.laser == 0:
			if enemy.laser_time + 4000 <= enemy.current:
				enemy.laser = 1
				enemy.laser_time = pygame.time.get_ticks()
		elif enemy.laser == 1:
			if enemy.laser_time + 2500 <= enemy.current:
				add_enemy_laser(ai, screen, ship, enemy, lasers)
				enemy.laser = 2
				enemy.laser_time = pygame.time.get_ticks()
		elif enemy.laser == 2:
			if enemy.laser_time + 2200 <= enemy.current:
				enemy.laser = 0
				enemy.laser_time = pygame.time.get_ticks()

		# Homing Bullets
		if enemy.start + 1250 <= enemy.current:
			enemy.homing = 1
			enemy.spray = 0
			add_enemy_bullets(ai, var, screen, ship, enemy, slayers)
			enemy.start = pygame.time.get_ticks()
			
def add_enemy_bullets(ai, var, screen, ship, enemy, slayers):
	"""Creation of an enemy bullet."""
	if enemy.homing:
		slay = Slay(ai, screen, ship, enemy, 1, 0)
		slayers.add(slay)
	elif enemy.spray:
		for m in range(((-1)*enemy.s_amount), (enemy.s_amount + 1)):
			slay = Slay(ai, screen, ship, enemy, 2, m)
			slayers.add(slay)
	else:
		slay = Slay(ai, screen, ship, enemy, 0, 0)
		slayers.add(slay)
	
def enemy_laser(ai, screen, ship, enemy, lasers):
	"""Creation and processes of enemy laser."""
	laser = Laser(ai, screen, ship, enemy, 0)
	lasers.add(laser)

def add_enemy_laser(ai, screen, ship, enemy, lasers):
	"""Creation and processes of enemy laser."""
	laz = Laser(ai, screen, ship, enemy)
	lasers.add(laz)
