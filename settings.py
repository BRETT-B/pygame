import pygame

class Settings():
	def __init__(self):
		self.screen_size = (1000,800)
		self.bg_color = (82,111,53)
		self.bullet_speed = 8
		self.bullet_width = 4
		self.bullet_height = 8
		self.bullet_color = 0,0,0
		self.enemy_speed = 4
		self.game_active = False