import math

class Settings():
	"""A class to store all settings."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen Settings
		self.width = 1200
		self.height = 800
		self.color = (150, 150, 150)
		
		# Static Image Settings
		self.static_speed = 0.25
		
		# Background Settings
		self.background_speed = 1.75
		self.back = 1
		
		# Ship Settings
		self.speed_ratio = 1.25
		
		# Bullet Settings
		self.b1_width = 20
		self.b1_height = 6
		self.b1_color = (219, 87, 163) # pink
		self.b2_color = (249, 126, 17) # orange
		self.b3_color = (198, 23, 236) # purple
		self.b4_color = (255, 0, 0) # Red
		self.b5_color = (48, 184, 229) # light blue
		self.b1_speed = 10
		
		# Enemy Settings
		self.e_speed = 10
		self.e_direction = 1
		self.e_range = 10
		self.e_move = 1
		self.e_hp = [20, 5, 2, 100, 10]
		self.e_score = [750, 350, 200, 5000, 1250]
		
		# Other
		# self.osc = math.pi/2
		self.wave = 1
