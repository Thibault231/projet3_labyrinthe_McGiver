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
	mac_giver.show_element(window_surface)
	guardian.show_element(window_surface)

	# execute the game script for events
	launched = True
	
	while launched:
	    
	    for event in pygame.event.get():
	        
	        if event.type == pygame.QUIT:
	            launched = False
	        if event.type == KEYDOWN:
				if event.key == K_DOWN:
					#Colisions cheking
					#MacGyver movement
					#running interractions with items and guardian
					pass
				elif event.key == K_UP:
					#Colisions cheking
					#MacGyver movement
					#running interractions with items and guardian
					pass
				elif event.key == K_RIGHT:
					#Colisions cheking
					#MacGyver movement
					#running interractions with items and guardian
					pass
				elif event.key == K_UP:
					#Colisions cheking
					#MacGyver movement
					#running interractions with items and guardian
					pass
				else:
					pass
		
		pygame.display.flip()
	
	pygame.mixer.music.stop()
	pygame.quit()

		
main()


