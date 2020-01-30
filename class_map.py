#coding: utf-8
import numpy as np 
import pygame

""" 
This module rule the map of the game.
"""
def repare_labyrinth(window_surface, x_position, y_position):
	""" Pastes labyrinth texture on the map after Mac Gyver's movment"""
	labyrinth_path = pygame.image.load("pictures/labyrinth_path.jpg") #  
	labyrinth_path.convert_alpha()
	window_surface.blit(labyrinth_path, [x_position,y_position])

def map_coord_set(mark):
			""" Extracte coordonates of labyrinth's element and set them in a list of tupples"""
			with open("labyrinthe.txt", "r") as f :
				fichier_entier = f.read()
				files = fichier_entier.split("\n")

			map_lab=[]
			for row in files:
				row_cells = [cell for cell in row]
				map_lab.append(row_cells)
			coord_on_map=[]
			for row in range (0,len(map_lab)):
				for column in range(0, len(map_lab)):
					if map_lab[row][column] == mark:
						coord_on_map.append((row+1,column+1))
			return coord_on_map

class Map:
	""" 
	Create the class Map for mapping the game as a matrix.
	Map's creating objects need two arguments.
	"""
	
	def __init__(self, width, heigth):
		"""  Initiate the map attribute according to two size variables. """
		self.map = np.zeros((width, heigth))
		self.pos_start = map_coord_set("h")
		self.pos_GD = map_coord_set("g")
		self.lab_path = map_coord_set("o")
		self.full_lab = self.pos_start + self.pos_GD + self.lab_path

	def show_labyrinth(self, window_surface):
		""" Display the labyrinth on Pygame window."""

		# define texture for the labyrinth path and wall
		labyrinth_path = pygame.image.load("pictures/labyrinth_path.jpg") #  
		labyrinth_path.convert_alpha()
		labyrinth_wall = pygame.image.load("pictures/labyrinth_wall.jpg") #  
		labyrinth_path.convert_alpha()

		# create liste of 15 rows from plan on laby.txt.
		with open("labyrinthe.txt", "r") as f:
			fichier_entier = f.read()
			files = fichier_entier.split("\n")
		# create list of 15*15 cells
		map_lab=[]
		for row in files:
			row_cells = [cell for cell in row]
			map_lab.append(row_cells)
		# display labyrinth
		for row in range (0,len(map_lab)):
			for column in range(0, len(map_lab)):
				# define texture square of 40*40 pixels
				x_position = ((row) * 40) 
				y_position = ((column) * 40)
				if map_lab[row][column] == "m":
					window_surface.blit(labyrinth_wall, [y_position,x_position])
				else:
					window_surface.blit(labyrinth_path, [y_position,x_position])
		pygame.display.flip()

