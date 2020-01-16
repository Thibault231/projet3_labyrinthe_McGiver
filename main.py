#coding: utf-8
import numpy as np 
import time
import pygame
from pygame.locals import *

from class_map import *
from class_item import *
from class_character import *
from class_element import *

def main():
	
	# create map, items and characters with their positions
	map_game = Map(15, 15)
	list_items = items_settlement()
	MacGuffin =list_items.pop()
	mac_gyver, guardian = characters_settlement(MacGuffin)
	# create and display the pygame main window surface	
	pygame.init()
	window_resolution = (600, 600)
	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)   # surface object
	pygame.display.flip()

	#creates starts playlist songs.
	pygame.mixer.music.load("songs/InClosing-DaysPast.mp3")
	pygame.mixer.music.play()

	# display labyrinth, items and characters on the main surface
	map_game.show_labyrinth(window_surface)
	for item in list_items:
		item.show_element(window_surface)
	mac_gyver.show_element(window_surface)
	guardian.show_element(window_surface)

	# execute the game script for events
	launched = True
	
	while launched:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				launched = False

			elif event.type == KEYDOWN and event.key == K_DOWN:
				mac_gyver.character_movment("down", window_surface,
				 mac_gyver.position[0],  mac_gyver.position[1] )
			elif event.type == KEYDOWN and event.key == K_UP:
				mac_gyver.character_movment("up", window_surface,
				 mac_gyver.position[0],  mac_gyver.position[1] )

			elif event.type == KEYDOWN and event.key == K_RIGHT:
				mac_gyver.character_movment("right", window_surface,
				 mac_gyver.position[0],  mac_gyver.position[1] )

			elif event.type == KEYDOWN and event.key == K_LEFT:
				mac_gyver.character_movment("left", window_surface,
				 mac_gyver.position[0],  mac_gyver.position[1] )
			else:
				pass

	pygame.display.flip()
	
	pygame.mixer.music.stop()
	pygame.quit()

		
main()


