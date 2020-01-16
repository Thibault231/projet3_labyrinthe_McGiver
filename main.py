#coding: utf-8
import numpy as np 
import pygame

from class_map import *
from class_item import *
from class_character import *
from class_element import *

def main():
	# create map, items and characters with their positions
	map_game = Map(15, 15)
	list_items = items_settlement()
	MacGuffin =list_items.pop()
	mac_giver, guardian = characters_settlement(MacGuffin)

	
	# create and display the pygame main window surface	
	pygame.init()
	window_resolution = (600, 600)
	launched = True

	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)   # surface object
	pygame.display.flip()

	# display labyrinth, items and characters on the main surface
	map_game.show_labyrinth(window_surface)
	for item in list_items:
		item.show_element(window_surface)
	mac_giver.show_element(window_surface)
	guardian.show_element(window_surface)

	while launched:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            launched = False
	    
		#pygame.display.flip()


main()


