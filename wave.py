import pygame

class Wave():
	"""Variables that control the wave of enemies."""
	
	def __init__(self, ai, var):
		self.ai = ai
		self.var = var
		
		self.start = 0
		self.current = 0
		self.counter = 1
		self.entrances = 0
