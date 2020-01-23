#coding: utf-8
import random
import time
import numpy as np 
import pygame

from class_map import Map, repare_labyrinth
from class_element import Element, Character, Item

""" 
This module rule the start positions of characters and
items on the map.
"""



def characters_settlement(MacGuffin):
	""" Define Characters and there positions on the labyrinth map"""
	
	# Characters creations
	mac_giver = Character("Mac","pictures/MacGyver.png")
	mac_giver.position = Map.MAP_LABYRINTH[0]
	mac_giver.element_sizing_position()
	guardian = Character("Guardian","pictures/Gardien.png")
	guardian.position = Map.MAP_LABYRINTH[-1]
	guardian.element_sizing_position()

	return mac_giver, guardian


def items_settlement():
	""" Define items and there position on the labyrinth map"""
	
	# items creations
	needle = Item ("needle","pictures/needle.png")
	seringe = Item ("seringe","pictures/seringe.png")
	ether = Item ("ether","pictures/ether.png")
	MacGuffin = Item ("MacGuffin","pictures/MacGyver.png")
	
	#lists of items and random positions creation 
	#(exept the guardian's position)
	list_items = [needle, seringe, ether, MacGuffin ]
	list_random_position = list(Map.MAP_LABYRINTH)
	list_random_position.remove(Map.MAP_LABYRINTH[-1])
	list_random_position.remove(Map.MAP_LABYRINTH[1])
	random.shuffle(list_random_position)
	
	# random positions attribution
	for i in range(len(list_items)):
		item = list_items[i]
		item.position = list_random_position[i]
		item.element_sizing_position()
		print(item.name, "posséde la position  ", item.position)

	return list_items