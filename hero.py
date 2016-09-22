import pygame
import sys

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen

		# Load the hero image, get it's rect
		self.image = pygame.image.load('img/ball.gif')
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object for location
		self.screen_rect = screen.get_rect() #assign a var so the hero knows how
		# SET THE X AND Y COORDINATES
		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero at the "bottom" of the screen

		self.moving_right = False
		self.moving_left = False
		# self.moving_up = False
		# self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10
		elif self.moving_left and self.rect.left < self.screen_rect.left:
			self.rect.centerx -= 10
	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect) #draw the surface...(the image, the where)