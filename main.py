#coding: utf-8
import pygame
from pygame.locals import *

from class_map import *
from settlements import *
from classes import *
from fonction_deplacement import*

def main():
	
	# create map, items and characters with their positions
	map_game = Map(15, 15)
	list_items = items_settlement()
	MacGuffin =list_items.pop()
	mac_gyver, guardian = characters_settlement(MacGuffin)
	
	# creates and displays the pygame main window surface	
	pygame.init()
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
				launched = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_UP:
				movement(mac_gyver, window_surface, 0, -1)
				list_items = items_control(mac_gyver, list_items)
				launched = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_RIGHT:
				movement(mac_gyver, window_surface, 1, 0)
				list_items = items_control(mac_gyver, list_items)
				launched = guardian_checking(launched, mac_gyver)

			elif event.type == KEYDOWN and event.key == K_LEFT:
				movement(mac_gyver, window_surface, -1, 0)
				list_items = items_control(mac_gyver, list_items)
				launched = guardian_checking(launched, mac_gyver)
			
	pygame.display.flip()
	pygame.mixer.music.stop()
	pygame.quit()

		
main()


