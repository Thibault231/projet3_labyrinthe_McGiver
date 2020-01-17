#coding: utf-8
import random
import numpy as np 
import pygame
import time

from class_map import *
from fonction_deplacement import *

class Element:
	""" 
	Define the parent class for characters and items
	"""

	def __init__(self, name, picture_path, x_position=0, y_position=0):
			"""  Initiate common element's attributs """
			self.name = name
			self.picture_path = picture_path 
			self.position = [x_position, y_position]


	def element_sizing_position(self):
		""" Transforms matrix coordonates in surface set of 
		coordonates for the Pygame window. Transform element. """
		
		(x_position, y_position) = self.position
		self.position = [ (y_position - 1) * 40 + 10,
		 (x_position - 1) * 40 + 10]

	def revsizing_position(self):
		""" Transforms window's coordonates in matrix
		set of coordonates. Return coordonates"""	
		y_position, x_position = self.position[1], self.position[0]
		y_position =  (y_position - 10) / 40 + 1
		x_position = (x_position - 10) / 40 + 1
		return x_position, y_position

	def show_element(self, window_surface):
		""" Display elements randomly in the labyrinth on Pygame window."""

		element = pygame.image.load(self.picture_path) #  
		element.convert_alpha()
		# display element's picture in the labyrinth
		window_surface.blit(element, self.position)
		pygame.display.flip()



class Character(Element):
	"""
	Define the class which is used for creating  Mac Giver
	and the guardian.
	"""

	def __init__(self, name, picture_path, x_position=0, y_position=0):
			"""  Initiate characters attributs """
			super().__init__(name, picture_path, x_position, y_position)
			self.counter = 0

	def _new_position(self):
		""" Identification of futur Mac Gyver's position on the map"""
		
		y_position, x_position = self.position
		y_position = (y_position + y_var) * 40
		x_position = (x_position + x_var) * 40

		return(self.position)

	

class Item(Element):
	"""
	Define a children class for all items which should 
	be collected by Mac Giver
	"""