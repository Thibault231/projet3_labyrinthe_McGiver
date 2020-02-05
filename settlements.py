#coding: utf-8
import random
import time
import numpy as np 
import pygame

from map import Map, repare_labyrinth
from element import Element
from character import Character
from item import Item

""" 
This module rule the start positions of characters and
items on the map.
"""

def characters_settlement(map_game):
	""" Define Characters and there positions on the labyrinth map"""
	
	# Characters creations
	mac_giver = Character("Mac","pictures/MacGyver.png")
	mac_giver.position = map_game.pos_start[0]
	mac_giver.element_sizing_position()
	guardian = Character("Guardian","pictures/Gardien.png")
	guardian.position = map_game.pos_GD[0]
	guardian.element_sizing_position()
	return mac_giver, guardian

def items_settlement(map_game):
	""" Define items and there position on the labyrinth map"""
	
	# items creations
	needle = Item ("needle","pictures/needle.png")
	seringe = Item ("seringe","pictures/seringe.png")
	ether = Item ("ether","pictures/ether.png")
	
	#creation of items list and their  random positions 
	#(exept the guardian and Mac Gyver's positions)
	list_items = [needle, seringe, ether]
	list_random_position = list(map_game.lab_path)
	random.shuffle(list_random_position)
	
	# random positions attribution
	for i in range(len(list_items)):
		item = list_items[i]
		item.position = list_random_position[i]
		item.element_sizing_position()
		#print(item.name, "posséde la position  ", item.position)
	return list_items