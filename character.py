#coding: utf-8
import random
import numpy as np 
import pygame
import time

from map import Map
from element import Element
""" 
This module rule items and characters classes as heritated
from the parent class: Element.
"""
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