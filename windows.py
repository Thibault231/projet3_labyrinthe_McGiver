#coding: utf-8
import pygame
from pygame.locals import *

""" 
Module ruling the start and end windows.
"""

def start_window():
	window_resolution = (600, 600)
	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)
	pygame.display.flip()

	pygame.mixer.music.load("songs/Savfk_TheImpossible.mp3") 
	pygame.mixer.music.play()	

	labyrinth_font = pygame.image.load("pictures/your_mission.jpg")
	labyrinth_font.convert_alpha()
	window_surface.blit(labyrinth_font, [0, 0])
	pygame.display.flip()

	launched = True
	while launched:
		for event in pygame.event.get():
			# Quit the loop if player close the window
			if event.type == pygame.QUIT:
				launched = False
			elif event.type == KEYDOWN and event.key == K_RETURN:
				launched = False

def end_window(end_game):
	window_resolution = (600, 600)
	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)
	pygame.display.flip()

		# select the end picture to display
	if end_game:
		labyrinth_font = pygame.image.load("pictures/you_die.jpg")
		pygame.mixer.music.load("songs/Savfk_TheImpossible.mp3") 
	elif not end_game:
		labyrinth_font = pygame.image.load("pictures/you_win.jpg") 
		pygame.mixer.music.load("songs/KSoviet04Final.mp3")
	
	pygame.mixer.music.play()
	labyrinth_font.convert_alpha()
	window_surface.blit(labyrinth_font, [0, 0])
	pygame.display.flip()

	launched = True
	while launched:
		for event in pygame.event.get():
			# Quit the loop if player close the window
			if event.type == pygame.QUIT:
				launched = False
			elif event.type == KEYDOWN and event.key == K_RETURN:
				launched = False