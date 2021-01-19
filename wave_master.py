import pygame
from wave import Wave
from enemy import Enemy

def wave_master(ai, var, screen, ship, enemies, wave):
	"""Checks enemies and begings the new wave."""
	#wave.counter = 4
	if wave.entrances == 1:
		wave.current = pygame.time.get_ticks()
		if wave.counter == 1:
			wave_1(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 2:
			wave_2(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 3:
			wave_3(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 4:
			wave_4(ai, var, screen, ship, enemies, wave)			
		elif wave.counter == 5:
			wave_5(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 6:
			wave_6(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 7:
			wave_7(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 8:
			wave_8(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 9:
			wave_9(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 10:
			wave_10(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 11:
			wave_11(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 12:
			wave_12(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 13:
			wave_13(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 14:
			wave_14(ai, var, screen, ship, enemies, wave)		
		elif wave.counter == 15:
			wave_15(ai, var, screen, ship, enemies, wave)		
		elif wave.counter == 16:
			wave_16(ai, var, screen, ship, enemies, wave)		
		elif wave.counter == 17:
			wave_17(ai, var, screen, ship, enemies, wave)		
		elif wave.counter == 18:
			wave_18(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 19:
			wave_19(ai, var, screen, ship, enemies, wave)
		elif wave.counter == 20:
			wave_20(ai, var, screen, ship, enemies, wave)
			
def wave_1(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 1, ((ai.height/2)))
			enemies.add(enemy)
			wave.entrances = 0
			wave.counter += 1

def wave_2(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 1, ((ai.height/3)))
			enemies.add(enemy)
	if wave.start + 3500 <= wave.current:
		if len(enemies) == 1:
			enemy2 = Enemy(ai, var, screen, ship, 1, (2*(ai.height/3)))
			enemies.add(enemy2)
			wave.entrances = 0
			wave.counter += 1

def wave_3(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 1, ((ai.height/3)))
			enemies.add(enemy)
	if wave.start + 3500 <= wave.current:
		if len(enemies) == 1:
			enemy2 = Enemy(ai, var, screen, ship, 1, ((ai.height/2)))
			enemies.add(enemy2)
	if wave.start + 5000 <= wave.current:
		if len(enemies) == 2:
			enemy3 = Enemy(ai, var, screen, ship, 1, (2*(ai.height/3)))
			enemies.add(enemy3)
			wave.entrances = 0
			wave.counter += 1

def wave_4(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 1, ((ai.height/2)))
			enemy5 = Enemy(ai, var, screen, ship, 2, ((ai.height/3)))
			enemy6 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/3)))
			enemies.add(enemy5)
			enemies.add(enemy6)
			enemies.add(enemy)
	if wave.start + 3500 <= wave.current:
		if len(enemies) == 3:
			enemy2 = Enemy(ai, var, screen, ship, 2, ((ai.height/3)))
			enemy3 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/3)))
			enemies.add(enemy2)
			enemies.add(enemy3)
			wave.entrances = 0
			wave.counter += 1

def wave_5(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemy2 = Enemy(ai, var, screen, ship, 2, ((ai.height/3)))
			enemy3 = Enemy(ai, var, screen, ship, 2, ((ai.height/3)+40))
			enemies.add(enemy)
			enemies.add(enemy2)
			enemies.add(enemy3)
	if wave.start + 3500 <= wave.current:
		if len(enemies) == 3:
			enemy4 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/3)))
			enemy5 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/3)-40))
			enemies.add(enemy4)
			enemies.add(enemy5)
			wave.entrances = 0
			wave.counter += 1

def wave_6(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 2, ((ship.rect.y)))
			enemies.add(enemy)
	if wave.start + 3000 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemy3 = Enemy(ai, var, screen, ship, 2, ((ship.rect.y)))
			enemies.add(enemy2)
			enemies.add(enemy3)
	if wave.start + 5000 <= wave.current:
		if len(enemies) <= 3:
			enemy4 = Enemy(ai, var, screen, ship, 2, ((ship.rect.y)))
			enemies.add(enemy4)
	if wave.start + 7000 <= wave.current:
		if len(enemies) <= 4:
			enemy5 = Enemy(ai, var, screen, ship, 2, ((ship.rect.y)))
			enemies.add(enemy5)
			wave.entrances = 0
			wave.counter += 1

def wave_7(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:	
			enemy = Enemy(ai, var, screen, ship, 1, ((ai.height/3)))
			enemy2 = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemy3 = Enemy(ai, var, screen, ship, 1, (2*(ai.height/3)))
			enemies.add(enemy)
			enemies.add(enemy2)
			enemies.add(enemy3)
			wave.entrances = 0
			wave.counter += 1
				
def wave_8(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:	
			enemy = Enemy(ai, var, screen, ship, 0, ((ai.height/3)))
			enemy2 = Enemy(ai, var, screen, ship, 1, ((ai.height/2)))
			enemy3 = Enemy(ai, var, screen, ship, 0, (2*(ai.height/3)))
			enemies.add(enemy)
			enemies.add(enemy2)
			enemies.add(enemy3)
			wave.entrances = 0
			wave.counter += 1
			
def wave_9(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemies.add(enemy)
	if wave.start + 3000 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 0, ((ai.height/3)))
			enemy3 = Enemy(ai, var, screen, ship, 0, (2*(ai.height/3)))
			enemies.add(enemy2)
			enemies.add(enemy3)
	if wave.start + 4000 <= wave.current:
		if len(enemies) <= 3:
			enemy4 = Enemy(ai, var, screen, ship, 2, ((ship.rect.y)))
			enemies.add(enemy4)
			wave.entrances = 0
			wave.counter += 1
	
def wave_10(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 4, ((ai.height/3)))
			enemies.add(enemy)
	if wave.start + 3777 <= wave.current:
		if len(enemies) <= 1:
			enemy = Enemy(ai, var, screen, ship, 4, (2*(ai.height/3)))
			enemies.add(enemy)
			wave.entrances = 0
			wave.counter += 1

def wave_11(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 4, ((ai.height/3)))
			enemies.add(enemy)
	if wave.start + 3250 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 4, (2*(ai.height/3)))
			enemies.add(enemy2)
			wave.entrances = 0
			wave.counter += 1
			
def wave_12(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 4, ((ai.height/3)))
			enemies.add(enemy)
	if wave.start + 3750 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 4, (2*(ai.height/3)))
			enemies.add(enemy2)
	if wave.start + 8000 <= wave.current:
		if len(enemies) <= 2:
			enemy3 = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemies.add(enemy3)		
			wave.entrances = 0
			wave.counter += 1

def wave_13(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 4, ((ai.height/2)))
			enemies.add(enemy)
	if wave.start + 3750 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 1, (2*(ai.height/3)))
			enemies.add(enemy2)
	if wave.start + 4250 <= wave.current:
		if len(enemies) <= 2:
			enemy3 = Enemy(ai, var, screen, ship, 1, ((ai.height/3)))
			enemies.add(enemy3)
	if wave.start + 7500 <= wave.current:
		if len(enemies) <= 3:
			enemy4 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/5)))
			enemy5 = Enemy(ai, var, screen, ship, 2, (4*(ai.height/5)))
			enemies.add(enemy4)		
			enemies.add(enemy5)		
			wave.entrances = 0
			wave.counter += 1

def wave_14(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemies.add(enemy)
	if wave.start + 3457 <= wave.current:
		if len(enemies) <= 1:
			enemy2 = Enemy(ai, var, screen, ship, 0, (2*(ai.height/3)))
			enemy3 = Enemy(ai, var, screen, ship, 0, ((ai.height/3)))
			enemy4 = Enemy(ai, var, screen, ship, 2, (2*(ai.height/3)))
			enemy5 = Enemy(ai, var, screen, ship, 2, ((ai.height/3)))
			enemies.add(enemy2)
			enemies.add(enemy3)
			enemies.add(enemy4)
			enemies.add(enemy5)
			wave.entrances = 0
			wave.counter += 1

def wave_15(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 4, (2*(ai.height/6)))
			enemies.add(enemy)
	if wave.start + 3250 <= wave.current:
		if len(enemies) == 1:
			enemy2 = Enemy(ai, var, screen, ship, 4, (5*(ai.height/6)))
			enemies.add(enemy2)
	if wave.start + 4500 <= wave.current:
		if len(enemies) == 2:
			enemy3 = Enemy(ai, var, screen, ship, 4, (3*(ai.height/6)))
			enemies.add(enemy3)
	if wave.start + 5750 <= wave.current:
		if len(enemies) == 3:
			enemy4 = Enemy(ai, var, screen, ship, 4, (4*(ai.height/6)))
			enemies.add(enemy4)
			wave.entrances = 0
			wave.counter += 1

def wave_16(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 3, ((ai.height/2)))
			enemies.add(enemy)
			wave.entrances = 0
			wave.counter += 1

def wave_17(ai, var, screen, ship, enemies, wave):
	if wave.start + 2000 <= wave.current:
		if len(enemies) == 0:
			enemy = Enemy(ai, var, screen, ship, 0, ((ai.height/2)))
			enemies.add(enemy)
			wave.entrances = 0
			wave.counter += 1
