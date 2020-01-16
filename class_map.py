#coding: utf-8
import numpy as np 
import pygame

class Map:
	""" 
	Create the class Map for mapping the game as a matrix.
	Map's creating objects need two arguments.
	"""
	# The last tuple should be the exit coordonates
	MAP_LABYRINTH=[
(2,8),
(3,8), (3,9),(3,10),(3,11), (3,12), 
(4,3),(4,4),(4,11),(4,12),
(5,3),(5,4),(5,5),(5,12),
(6,5),(6,12),(6,11),(6,10),(6,9),(6,8),
(7,5),(7,6),(7,8),
(8,8),(8,7),(8,6),(8,5),
(9,8),
(10,8),(10,9),(10,10),(10,11),(10,12),(10,13),(10,14),
(11,8),(11,13),(11,14),
(12,8),
(13,8),(13,9),
(14,8),(14,9),
(15,9)
]

	def __init__(self, width, heigth):
		"""  Initiate the map attribute according to two size variables. """
		self.map = np.zeros((width, heigth))


	def show_labyrinth(self, window_surface):
		""" Display the labyrinth on Pygame window."""
		# define font picture
		labyrinth_font = pygame.image.load("pictures/labyrinth_font.jpg") 
		labyrinth_font.convert_alpha()
		window_surface.blit(labyrinth_font, [0, 0])
		# define texture for the labyrinth path
		labyrinth_path = pygame.image.load("pictures/labyrinth_path.jpg") #  
		labyrinth_path.convert_alpha()
		
		# display texture for the labyrinth on window_surface
		for (row, column) in self.MAP_LABYRINTH:
			# define texture square of 40*40 pixels
			x_position = ((row - 1) * 40) +10  
			y_position = ((column - 1) * 40) + 10
			
			window_surface.blit(labyrinth_path, [y_position,x_position])
		
		pygame.display.flip()

def repare_labyrinth(window_surface, x_position, y_position):
	labyrinth_path = pygame.image.load("pictures/labyrinth_path.jpg") #  
	labyrinth_path.convert_alpha()
	window_surface.blit(labyrinth_path, [y_position,x_position])
