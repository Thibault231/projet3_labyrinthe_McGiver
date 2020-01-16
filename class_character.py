#coding: utf-8
import random
import time
import numpy as np 
import pygame

from class_map import *
from class_element import *

class Character(Element):
	"""
	Define the class which is used for creating  Mac Giver
	and the guardian.
	"""

	def __init__(self, name, picture_path, x_position=0, y_position=0):
			"""  Initiate characters attributs """
			self.name = name
			self.picture_path = picture_path 
			self.position = (x_position, y_position)

	def __new_position(self, direction):
		""" Identification of futur Mac Gyver's position on the map"""
		
		y_position, x_position = self.position
		self.position = ( (y_position + direction) * 40, 
			(x_position + direction) * 40)
		return(self.position)
	
	def character_movment(self, direction, window_surface, y_position, x_position ):
		"""Make Mac Giver moving on the labyrinth according to the
		directional key instructions translated by the key word 'direction' """

		#creates a fluent movment
		i = 1
		while i < 41:
			time.sleep(0.01)
			# select direcion and  moves mac_giver's picture 
			if direction == "right":
				self.position[0] += 1
				self.show_element(window_surface)
				pygame.display.flip()
				i +=1
			elif direction == "left":
				self.position[0] -= 1
				self.show_element(window_surface)
				pygame.display.flip()
				i +=1
			elif direction == "up":
				self.position[1] -= 1
				self.show_element(window_surface)
				pygame.display.flip()
				i +=1
			elif direction == "down":
				self.position[1] += 1
				self.show_element(window_surface)
				pygame.display.flip()
				i +=1	
		# corrects ugly overlay of mac_giver's hairstyle's images
		repare_labyrinth(window_surface, x_position, y_position)
		repare_labyrinth(window_surface, self.position[1], self.position[0])
		self.show_element(window_surface)
		pygame.display.flip()

def characters_settlement(MacGuffin):
	""" Define Characters and there positions on the labyrinth map"""
	
	# Characters creations
	mac_giver = Character ("Mac","pictures/MacGyver.png")
	mac_giver.position = MacGuffin.position
	guardian = Character ("Guardian","pictures/Gardien.png")
	guardian.position = Map.MAP_LABYRINTH[-1]
	guardian.element_sizing_position()

	return mac_giver, guardian


if __name__ == "__main__": 
	mac_giver = Character ("Mac","pictures/MacGyver.png", 8 , 4)
	print(mac_giver.position[0])
	#mac_giver.character_movment(1, 1)
