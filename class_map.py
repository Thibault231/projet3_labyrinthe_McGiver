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

def map_as_list():
	""" Extracte coordonates of labyrinth's path and set them in a list of tupples"""
	with open("laby.txt", "r") as f :
		fichier_entier = f.read()
		files = fichier_entier.split("\n")

	map_lab=[]
	for row in files:
		row_cells = [cell for cell in row]
		map_lab.append(row_cells)
	MAPPY=[]
	for row in range (0,len(map_lab)):
		for column in range(0, len(map_lab)):
			if map_lab[row][column] in ["o","h","g"]:
				MAPPY.append((row+1,column+1))
	return MAPPY


class Map:
	""" 
	Create the class Map for mapping the game as a matrix.
	Map's creating objects need two arguments.
	"""
	# Last tuple is the exit position, First is Mac position
	MAP_LABYRINTH = map_as_list()

	def __init__(self, width, heigth):
		"""  Initiate the map attribute according to two size variables. """
		self.map = np.zeros((width, heigth))

	def show_labyrinth(self, window_surface):
		""" Display the labyrinth on Pygame window."""

		# define texture for the labyrinth path and wall
		labyrinth_path = pygame.image.load("pictures/labyrinth_path.jpg") #  
		labyrinth_path.convert_alpha()
		labyrinth_wall = pygame.image.load("pictures/labyrinth_wall.jpg") #  
		labyrinth_path.convert_alpha()

		# create liste of 15 rows from plan on laby.txt.
		with open("laby.txt", "r") as f:
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
				x_position = ((row) * 40) +10  
				y_position = ((column) * 40) + 10
				if map_lab[row][column] == "m":
					window_surface.blit(labyrinth_wall, [y_position,x_position])
				else:
					window_surface.blit(labyrinth_path, [y_position,x_position])
		pygame.display.flip()


if __name__=="__main__":
	with open("laby.txt", "r") as f :
	    fichier_entier = f.read()
	    files = fichier_entier.split("\n")

	map_lab=[]
	for row in files:
		row_cells = [cell for cell in row]
		map_lab.append(row_cells)
	MAPPY=[]
	for row in range (0,len(map_lab)):
		for column in range(0, len(map_lab)):
			if map_lab[row][column] in ["o","h","g"]:
				MAPPY.append((row,column))
	print (MAPPY)

