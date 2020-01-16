#coding: utf-8
import random
import numpy as np 
import pygame

from class_map import *

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
		""" Resize matrix set of coordonates in surface set of 
		coordonates for the Pygame window """
		
		(x_position, y_position) = self.position
		self.position = [ (y_position - 1) * 40 + 10,
		 (x_position - 1) * 40 + 10]

	def show_element(self, window_surface):
		""" Display elements randomly in the labyrinth on Pygame window."""

		element = pygame.image.load(self.picture_path) #  
		element.convert_alpha()
		# display element's picture in the labyrinth
		window_surface.blit(element, self.position)
		pygame.display.flip()
