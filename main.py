#coding: utf-8
import pygame
from pygame.locals import *

from class_map import *
from class_element import *
from module_settlements import *
from module_events import *
from module_windows import *

""" 
Starting module executing the game program.
"""

def main():
	""" Run the main program"""

	pygame.init()
	
	# display the start window explaining the game
	start_window()	

	# create map, items and characters with their positions
	map_game = Map(15, 15)
	list_items = items_settlement()
	MacGuffin =list_items.pop()
	mac_gyver, guardian = characters_settlement(MacGuffin)
	
	# creates and displays the pygame main window surface	
	window_resolution = (600, 600)
	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)   # surface object
	pygame.display.flip()

	#creates and starts playlist songs.
	pygame.mixer.music.load("songs/InClosing-DaysPast.mp3")
	pygame.mixer.music.play()

	# displays labyrinth, items and characters on the main surface
	map_game.show_labyrinth(window_surface)
	for item in list_items:
		item.show_element(window_surface)
	mac_gyver.show_element(window_surface)
	guardian.show_element(window_surface)

	# execution of game's script for the events
	launched = True
	end_game = True
	while launched:

		for event in pygame.event.get():
			# Quit the loop if player close the window
			if event.type == pygame.QUIT:
				launched = False
			# Events for directional keys
			elif event.type == KEYDOWN and event.key == K_DOWN:
				# Make mac_gyver move
				movement(mac_gyver, window_surface, 0, 1)
				# Control interraction with items
				list_items = items_control(mac_gyver, list_items)
				# Control interaction with the guardian
				launched, end_game = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_UP:
				movement(mac_gyver, window_surface, 0, -1)
				list_items = items_control(mac_gyver, list_items)
				launched, end_game = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_RIGHT:
				movement(mac_gyver, window_surface, 1, 0)
				list_items = items_control(mac_gyver, list_items)
				launched, end_game = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_LEFT:
				movement(mac_gyver, window_surface, -1, 0)
				list_items = items_control(mac_gyver, list_items)
				launched, end_game = guardian_checking(launched, mac_gyver)
	pygame.mixer.music.stop()
	

	# display and happy or unhappy ending window.
	end_window(end_game)
pygame.quit()
		
main()


