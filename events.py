#coding: utf-8
import pygame
import time
from pygame.locals import *

from class_map import Map, repare_labyrinth
from class_element import Element, Character, Item
from dialogs import display_speech

""" 
This module rule the movement and interactions events
during the game.
"""

def items_control(mac_gyver, list_items, window_surface ):
	""" Check that mac_gyver is or not on an item's cell.
	Implements the item's counter. """
	for item in list_items:

		if mac_gyver.position == item.position:
			mac_gyver.counter += 1
			display_speech(1, window_surface, mac_gyver.counter)
			list_items.remove(item)
	return list_items

def guardian_checking(launched, mac_gyver, map_game, end_game=True):
	""" Make mac_gyver escaping or dying when he
	comes on the guardian cell."""

	#Calculate mac_gyver position in the labyrinth matrix
	x_position, y_position = mac_gyver.revsizing_position()
	# Define the end according to the amont of collected items
	if (y_position, x_position) == map_game.pos_GD[0]:
		if mac_gyver.counter != 3:
			launched = False
			end_game = True
		elif mac_gyver.counter == 3:
			launched = False
			end_game = False
	return launched, end_game

def walls_control(mac_gyver, x_var, y_var, window_surface, map_game):
	""" Allowed or cancel mac_gyver's move depending
	on his next coordonates related to the labyrinth's map."""
	#Definine potentials mac_gyver's matricial coordonates
	x_position, y_position = mac_gyver.revsizing_position()
	x_position += x_var
	y_position += y_var
	# Allowed move if potential coordonates are in the labyrinth
	if (y_position, x_position) in map_game.full_lab:
		return x_var, y_var
	# Cancel move otherwise
	else:
		display_speech(2, window_surface, mac_gyver.counter)
		x_var = 0
		y_var = 0
		return x_var, y_var

def movement(self, window_surface, x_var, y_var, map_game):
		"""Make Mac Giver moving on the labyrinth according to the
		directional key instructions translated by the key word 'direction' """
		# forbides moves outside the labyrinth
		x_var, y_var = walls_control(self, x_var, y_var, window_surface, map_game)
		x_position, y_position = self.position[0], self.position[1]
		#creates a fluent movment
		i = 1
		while i < 41:
			time.sleep(0.01)
			# calculates mac_gyver next position  
			self.position[0] += x_var
			self.position[1] += y_var
			# Moves mac_giver's picture to his new position
			self.show_element(window_surface)
			pygame.display.flip()
			i +=1
		# corrects ugly overlay of mac_giver's hairstyle's images
		repare_labyrinth(window_surface, x_position, y_position)
		repare_labyrinth(window_surface, self.position[0], self.position[1])
		self.show_element(window_surface)
		pygame.display.flip()