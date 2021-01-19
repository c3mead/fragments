import pygame

class Variance():
	"""Place to store varied features in game."""
	
	def __init__(self):
		# Player Ship
		self.p_ship = []
		self.p_ship.append(pygame.image.load('images/ship/t_lship1.png'))
		self.p_ship.append(pygame.image.load('images/ship/t_lship1_up.png'))
		self.p_ship.append(pygame.image.load('images/ship/t_lship1_dn.png'))
		
		# Death Animaiton
		self.death = []
		self.death.append(pygame.image.load('images/effects/death/d_1.png'))
		self.death.append(pygame.image.load('images/effects/death/d_2.png'))
		self.death.append(pygame.image.load('images/effects/death/d_3.png'))
		self.death.append(pygame.image.load('images/effects/death/d_4.png'))
		self.death.append(pygame.image.load('images/effects/death/d_5.png'))
		self.death.append(pygame.image.load('images/effects/death/d_6.png'))
		self.death.append(pygame.image.load('images/effects/death/d_7.png'))
		self.death.append(pygame.image.load('images/effects/death/d_8.png'))
		
		# Different enemy ship images.
		self.b_ship = []
		self.b_ship.append(pygame.image.load('images/enemies/e_aship1.png'))
		self.b_ship.append(pygame.image.load('images/enemies/e_bship1.png'))
		self.b_ship.append(pygame.image.load('images/enemies/e_cship1.png'))
		self.b_ship.append(pygame.image.load('images/enemies/e_dship1.png'))
		self.b_ship.append(pygame.image.load('images/enemies/e_eship1.png'))
		
		# Different background images.
		self.o_back = []
		self.o_back.append(pygame.image.load('images/backgrounds/night4.png'))
		self.o_back.append(pygame.image.load('images/backgrounds/b1_hillside.png'))
		
		# Different static images
		self.o_stat = []
		self.o_stat.append(pygame.image.load('images/backgrounds/mountain_lake.png'))
		self.o_stat.append(pygame.image.load('images/backgrounds/b2_hillside.png'))
		
		# Different explosions
		self.explosion = []
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_1.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_2.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_3.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_4.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_5.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_6.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_7.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_8.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_9.png'))
		self.explosion.append(pygame.image.load('images/effects/shock/ehit_10.png'))

		# Charge Graphics
		self.charge = []
		self.charge.append(pygame.image.load('images/effects/charge/f_1.png'))
		self.charge.append(pygame.image.load('images/effects/charge/f_2.png'))
		self.charge.append(pygame.image.load('images/effects/charge/f_3.png'))
		self.charge.append(pygame.image.load('images/effects/charge/f_4.png'))
		self.charge.append(pygame.image.load('images/effects/charge/f_5.png'))
		self.charge.append(pygame.image.load('images/effects/charge/f_6.png'))
		self.charge2 = []
		self.charge2.append(pygame.image.load('images/effects/charge/f_1(2).png'))
		self.charge2.append(pygame.image.load('images/effects/charge/f_2(2).png'))
		self.charge2.append(pygame.image.load('images/effects/charge/f_3(2).png'))
		self.charge2.append(pygame.image.load('images/effects/charge/f_4(2).png'))
		self.charge2.append(pygame.image.load('images/effects/charge/f_5(2).png'))
		self.charge2.append(pygame.image.load('images/effects/charge/f_6(2).png'))
		

		# Buster Graphics
		self.buster = []
		self.buster.append(pygame.image.load('images/effects/buster/k_5.png'))
		self.buster.append(pygame.image.load('images/effects/buster/k_6.png'))
		self.buster.append(pygame.image.load('images/effects/buster/k_7.png'))
		self.buster.append(pygame.image.load('images/effects/buster/k_8.png'))
		
		# HP Display
		self.hp_bar = []
		self.hp_bar.append(pygame.image.load('images/hub/h_health_a.png'))
		self.hp_bar.append(pygame.image.load('images/hub/h_health_b.png'))
		
		# Shield Display
		self.s_bar = []
		self.s_bar.append(pygame.image.load('images/hub/h_health_a.png'))
		self.s_bar.append(pygame.image.load('images/hub/h_health_b.png'))
		
		# Title
		self.title = []
		self.title.append(pygame.image.load('images/hub/t_choice_a.png'))
		self.title.append(pygame.image.load('images/hub/t_choice_b.png'))
		self.title.append(pygame.image.load('images/hub/t_choice_c.png'))

		# Chapter
		self.chapters = []
		self.chapters.append(pygame.image.load('images/hub/r_chapter1.png'))
		
		# Health Item
		self.health = []
		#self.health.append(pygame.image.load('images/items/health/heart_1.png'))
		#self.health.append(pygame.image.load('images/items/health/heart_2.png'))
		self.health.append(pygame.image.load('images/items/health/heart_3.png'))
		self.health.append(pygame.image.load('images/items/health/heart_4.png'))
		self.health.append(pygame.image.load('images/items/health/heart_5.png'))
		self.health.append(pygame.image.load('images/items/health/heart_6.png'))
		self.health.append(pygame.image.load('images/items/health/heart_7.png'))
		self.health.append(pygame.image.load('images/items/health/heart_8.png'))
		self.health.append(pygame.image.load('images/items/health/heart_9.png'))
		self.health.append(pygame.image.load('images/items/health/heart_10.png'))
		
		# Ability Item
		self.ability = []
		self.ability.append(pygame.image.load('images/items/ability/ab_1.png'))
		self.ability.append(pygame.image.load('images/items/ability/ab_2.png'))
		self.ability.append(pygame.image.load('images/items/ability/ab_3.png'))
