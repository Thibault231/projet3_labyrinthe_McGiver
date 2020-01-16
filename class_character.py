#coding: utf-8
import random
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


def characters_settlement(MacGuffin):
	""" Define Characters and there positions on the labyrinth map"""
	
	# Characters creations
	mac_giver = Character ("Mac","pictures/MacGyver.png")
	mac_giver.position = MacGuffin.position
	guardian = Character ("Guardian","pictures/Gardien.png")
	guardian.position = Map.MAP_LABYRINTH[-1]
	guardian.element_sizing_position()

	return mac_giver, guardian
