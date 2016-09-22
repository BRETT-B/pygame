# We will put all main game functions here
import sys
import pygame



def check_events(hero):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

		# MOVE THE HERO
		elif event.type == pygame.KEYDOWN: #the user pressed a key
			if event.key == pygame.K_RIGHT:
				# Move the hero to the right
				hero.moving_right == True #set the flag
			elif event.key == pygame.K_LEFT:
				hero.moving_left == True #set the flag
		# STOP THE HERO MOVEMENT
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				hero.moving_right == False 
			elif event.key == pygame.K_LEFT:
				hero.moving_left == False
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color)
	hero.draw_me() #call the draw method imported from Hero class
	pygame.display.flip()