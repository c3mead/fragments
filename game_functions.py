import pygame, math, time, sys, random
from static import Static
from background import Background
from ship import Ship
from shooting import Shot
from enemy import Enemy
from slay import Slay
from shock import Shock
from charge import Charge
from shield import Shield
from wave import Wave
from blast import Blast
from hub import Hub
from item import Item
from death import Death

import wave_master as wm
import enemy_movements as em

def update_hub(ai, var, screen, ship, hub, deaths):
	hub.update(ai)
	if hub.h_bar <= 0:
		player_death(ai, var, screen, ship, hub, deaths)
	
def check_events(ai, var, screen, ship, shots, enemies, charges, shields, blasters, hub):
	"""Respond to keypresses, mouse events, and timed events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			key_down(event, ai, var, screen, ship, shots, enemies, charges, shields, hub)
		elif event.type == pygame.KEYUP:
			key_up(event, ai, var, screen, ship, charges, shields, blasters, hub)

def key_down(event, ai, var, screen, ship, shots, enemies, charges, shields, hub):
	"""Responds to key presses."""
	if event.key == pygame.K_UP:
		ship.move_up = 1
	elif event.key == pygame.K_DOWN:
		ship.move_down = 1
	elif event.key == pygame.K_SPACE:
		shoot_bullet(ai, screen, ship, shots, enemies)
		begin_charge(ai, var, screen, ship, charges)
	elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
		call_shield(ai, var, screen, ship, shields, hub)
	elif event.key == pygame.K_q:
		sys.exit()
	#elif event.key == pygame.K_p:
	#	hub.pause = 1
	elif event.key == pygame.K_z:
		hub.za_wurado(ai)
		
def key_up(event, ai, var, screen, ship, charges, shields, blasters, hub):
	"""Responds to key releases."""
	if event.key == pygame.K_UP:
		ship.move_up = 0
	elif event.key == pygame.K_DOWN:
		ship.move_down = 0
	elif event.key == pygame.K_SPACE:
		for charge in charges.copy():
			if charge.charge_level == 2:
				shoot_blaster(ai, var, screen, ship, blasters)
		ship.charge = 0
		charges.empty()
	elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
		if ship.shield:
			for shield in shields.copy():
				ship.shield = 0
				shields.empty()
		
def ship_updates(ai, var, screen, ship, charges, shields, hub):
	"""Updates and draws location of player ship."""
	ship.update(ai)
	ship.draw_ship()
	charge_shield_graphics(ai, var, screen, ship, charges, shields, hub)

def set_background(ai, var, screen, statics, backgrounds):
	"""Set-up multiple backgrounds"""	
	for stat in range(2):
		static = Static(ai, var, screen)
		static.x = ai.width * stat
		static.rect.x = static.x
		statics.add(static)
		
	for backs in range(2):
		background = Background(ai, var, screen)
		background.x = ai.width * backs
		background.rect.x = background.x
		backgrounds.add(background)

def loop_background(ai, var, screen, statics, backgrounds):
	"""Loops background for non-stop movement."""
	statics.update()
	for stat in statics.copy():
		if stat.rect.right <= 0:
			statics.remove(stat)
		if len(statics) < 2:
			static = Static(ai, var, screen)
			static.x = ai.width 
			static.rect.x = static.x
			statics.add(static)
	
	backgrounds.update()
	for back in backgrounds.copy():
		if back.rect.right <= 0:
			backgrounds.remove(back)
		if len(backgrounds) < 2:
			background = Background(ai, var, screen)
			background.x = ai.width 
			background.rect.x = background.x
			backgrounds.add(background)
			
	screen.fill(ai.color)
	statics.draw(screen)
	backgrounds.draw(screen)
	
def shoot_bullet(ai, screen, ship, shots, enemies):
	"""Shooting bullet functions."""
	if ship.s_count == 1:
		new_shot = Shot(ai, screen, ship, 1)
		shots.add(new_shot)
	if ship.s_count == 2:
		new_shot1 = Shot(ai, screen, ship, 2)
		new_shot2 = Shot(ai, screen, ship, 3)
		shots.add(new_shot1)
		shots.add(new_shot2)
	if ship.s_count == 3:
		new_shot1 = Shot(ai, screen, ship, 1)
		new_shot2 = Shot(ai, screen, ship, 2)
		new_shot3 = Shot(ai, screen, ship, 3)
		shots.add(new_shot1)
		shots.add(new_shot2)
		shots.add(new_shot3)
	
def shoot_blaster(ai, var, screen, ship, blasters):
	"""Shooting off a charged shot."""
	boom = Blast(ai, var, screen, ship)
	blasters.add(boom)
		
def begin_charge(ai, var, screen, ship, charges):
	"""Starts charge animation on ship."""
	if not ship.charge:
		ship.charge = 1
		charge = Charge(ai, var, screen, ship)
		charges.add(charge)

def call_shield(ai, var, screen, ship, shields, hub):
	"""Starts shield animation on ship."""
	if not hub.s_bar < 10:
		if not ship.shield:
			ship.shield = 1
			shield = Shield(ai, var, screen, ship, hub)
			shields.add(shield)
		
def charge_shield_graphics(ai, var, screen, ship, charges, shields, hub):
	"""Updates charge graphic animations"""
	if ship.charge == 1:
		for charge in charges.copy():
			charge.charge(screen, ship)
			charge.current2 = pygame.time.get_ticks()
			if charge.charge_level == 0:	
				if charge.start2 + 750 <= charge.current2:
					charge.charge_level = 1
					charge.start2 = pygame.time.get_ticks()
			
			elif charge.charge_level == 1:
				if charge.start2 + 1000 <= charge.current2:
					charge.charge_level = 2
					charge.start2 = pygame.time.get_ticks()
	if hub.s_bar >= 1:				
		if ship.shield == 1:
			for shield in shields.copy():
				shield.shield(screen, ship, hub)
		
def bullet_updates(ai, var, screen, ship, enemies, shots, blasters, 
	slayers, lasers, shockers, charges, shields, items, hub):
	# Remove old bullets
	for bullet in shots.copy():
		if bullet.rect.left >= ai.width:
			shots.remove(bullet)
	for blat in slayers.copy():
		if blat.rect.left <= 0:
			slayers.remove(blat)
	for boom in blasters.copy():
		if boom.rect.left >= ai.width:
			blasters.remove(boom)
	for laser in lasers.copy():
		if laser.gone == 1:
			lasers.remove(laser)
	
	# Draw new bullets		
	for shot in shots.sprites():
		shot.draw_shot()		
	for slay in slayers.sprites():
		slay.draw_shot()
	for blast in blasters.copy():
		blast.boom()
	for laser in lasers.sprites():
		laser.draw_laser()
		
	shots.update()
	slayers.update()
	item_updates(ai, var, screen, ship, items, hub)
		
	ship_bullet_hits(ai, var, screen, ship, enemies, shots, blasters, shockers, items, hub)
	enemy_bullet_hits(ai, screen, ship, enemies, slayers, lasers, shields, hub)
	
	pygame.sprite.groupcollide(blasters, slayers, False, True)

def laser_updates(ai, screen, ship, enemies, lasers):
	"""Laser trace and attack."""
	for enemy in enemies.copy():
		if enemy.laser == 1:
			enemy.y_y = enemy.rect.centery - ship.rect.centery
			enemy.x_x = enemy.rect.centerx - ship.rect.centerx
			enemy.m = float(enemy.y_y / enemy.x_x)
			enemy.b = enemy.rect.centery - (enemy.m * enemy.rect.centerx)
			enemy.t_y = (enemy.m * enemy.t_x) + enemy.b
			
			pygame.draw.line(screen, ai.b4_color, (enemy.t_x, enemy.t_y), 
				(enemy.rect.centerx, enemy.rect.centery), 2)
	for laser in lasers.copy():
		if laser.gone:
			lasers.remove(laser)

def ship_bullet_hits(ai, var, screen, ship, enemies, shots, blasters, shockers, items, hub):
	"""Checks for player bullet collisions on enemies."""
	for shot in shots.copy():
		if pygame.sprite.spritecollideany(shot, enemies):
			for enemy in enemies.copy():
				if pygame.sprite.spritecollideany(enemy, shots):
					enemy.hits += 1
					if enemy.hits >= enemy.hp:
						if not enemy.dead:
							item_chance(ai, var, screen, enemy, items, hub)
							enemy.dead = 1
							enemy.dead_time = pygame.time.get_ticks()
							enemy_death(ai, var, screen, enemy, shockers)
			shot.remove(shots)
			
	for blast in blasters.copy():
		if pygame.sprite.spritecollideany(blast, enemies):
			for enemy in enemies.copy():
				if pygame.sprite.spritecollideany(enemy, blasters):
					enemy.hits += 10
					if enemy.hits >= enemy.hp:
						if not enemy.boomed:
							enemy.boomed = 1
							enemy.t_boomed = pygame.time.get_ticks()
							item_chance(ai, var, screen, enemy, items, hub)
							enemy.dead = 1
							enemy.dead_time = pygame.time.get_ticks()
							enemy_death(ai, var, screen, enemy, shockers)

def enemy_death(ai, var, screen, enemy, shockers):
	"""Animation for a dying enemy and item chance"""
	shock = Shock(ai, var, screen, enemy)
	shockers.add(shock)

def enemy_bullet_hits(ai, screen, ship, enemies, slayers, lasers, shields, hub):
	"""Checks for enemy bullet collisions on player."""
	if ship.shield:
		pygame.sprite.groupcollide(slayers, shields, True, False)

	for slay in slayers.copy():
		if pygame.sprite.collide_rect(ship, slay):
			if not hub.death:
				hub.h_bar = hub.h_bar - slay.damage
				#ship.damage()
				slayers.remove(slay)
	
	for laser in lasers.copy():
		if laser.hurt:
			if pygame.sprite.collide_rect(ship, laser):
				if not hub.death:
					hub.h_bar = hub.h_bar - laser.damage
			
def enemy_load(ai, var, screen, ship, enemies):
	"""Loads the enemy ships."""
	for wav in range(2):
		if wav > 0:
			enemy = Enemy(ai, var, screen, ship, 4, (ai.height/3))
			enemy.y = (ai.height * wav) / (wav + 1)
			enemy.rect.centery = enemy.y
			enemies.add(enemy)
	
def enemy_update(ai, var, screen, ship, enemies, slayers, shockers, lasers, wave, hub):
	"""Update enemy position."""
	for enemy in enemies.copy():
		enemy.boom()
		if enemy.rect.left <= -10:
			enemies.remove(enemy)
		if not enemy.dead:
			em.load_movement(ai, var, screen, ship, enemy, slayers, lasers)
		else:
			if enemy.gone:
				hub.score = hub.score + enemy.score
				for laser in lasers.copy():
					lasers.remove(laser)
				enemies.remove(enemy)
			else:
				enemy.defeat()
	enemies.draw(screen) # If I place this below "shockers" group, explosion will be played under the image sprite

	# Enemy explosion animaiton
	if len(shockers) > 0:
		for enemy in enemies.copy():
			if enemy.dead:
				for laser in lasers.copy():
					lasers.remove(laser)
				for shock in shockers.copy():
					shock.explode(screen, enemy)
					if shock.gone:
						shockers.remove(shock)
				
	# Next wave of enemies			
	if len(enemies) <= 0:
		if wave.entrances == 0:
			wave.entrances = 1
			wave.start = pygame.time.get_ticks()
	wm.wave_master(ai, var, screen, ship, enemies, wave)
						
def item_chance(ai, var, screen, enemy, items, hub):
	if enemy.chance <= 45:
		e_poop = random.randint(1, 2)
		item = Item(ai, var, screen, enemy, hub, e_poop)
		items.add(item)
	
def item_updates(ai, var, screen, ship, items, hub):
	for item in items.copy():
		if pygame.sprite.collide_rect(ship, item):
			if item.type == 1:
				hub.h_bar += item.plus
			elif item.type == 2:
				hub.s_bar += item.plus
			items.remove(item)
		else:	
			item.update()
	
def player_death(ai, var, screen, ship, hub, deaths):
	hub.current = pygame.time.get_ticks()
	if not hub.death:
		hub.death = 1
		hub.timed = pygame.time.get_ticks() 
		hub.inputs = 1
		hub.ship = 1
		ded = Death(ai, var, screen, ship)
		deaths.add(ded)
	if hub.death <= 3:
		if hub.timed + 350 <= hub.current:
			ded = Death(ai, var, screen, ship)
			deaths.add(ded)
			hub.timed = pygame.time.get_ticks() 
			hub.death += 1
	
	for death in deaths.copy():
		death.death()
		if death.gone:
			deaths.remove(death)
	
def menu_screen(ai, screen, statics, backgrounds, ship, enemies, shots, slayers, hub):
	"""Menu Items."""
#	if hub.pause == 1:
#		#pygame.draw.rect(screen, (0, 0, 0), (0, 0, ai.width, ai.height))
#		for event in pygame.event.get():
#			if event.type == pygame.QUIT:
#				sys.exit()
#			elif event.type == pygame.KEYDOWN:
#				if event.key == pygame.K_p:
#					hub.pause = 0
	#ship.image.fill((255, 255, 255))
		
	pygame.display.flip()
