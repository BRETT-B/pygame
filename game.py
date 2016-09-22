
import pygame
from hero import Hero
from settings import Settings
import game_functions as gf


# Set up the main core function
def run_game():
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Monster Attack")
	hero = Hero(screen)
	while 1:
		gf.check_events(hero) #call gf (alias from game_functions) module and get check_events method
		hero.update() #update the hero flags
		gf.update_screen(game_settings, screen, hero) #call update screen method

run_game() #Start the game!
