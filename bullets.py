import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings):
		super(Bullet, self).__init__()
		self.screen == screen

		# Make a bullet
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		