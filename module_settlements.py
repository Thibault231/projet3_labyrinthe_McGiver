#coding: utf-8
import random
import time
import numpy as np 
import pygame

from class_map import *
from class_element import *
from module_events import *



def characters_settlement(MacGuffin):
	""" Define Characters and there positions on the labyrinth map"""
	
	# Characters creations
	mac_giver = Character("Mac","pictures/MacGyver.png")
	mac_giver.position = MacGuffin.position
	guardian = Character("Guardian","pictures/Gardien.png")
	guardian.position = Map.MAP_LABYRINTH[-1]
	guardian.element_sizing_position()

	return mac_giver, guardian


def items_settlement():
	""" Define items and there position on the labyrinth map"""
	
	# items creations
	burger = Item ("burger","pictures/burger.png")
	hammer = Item ("hammer","pictures/hammer.png")
	knife = Item ("knife","pictures/knife.png")
	nail = Item ("nail","pictures/nail.png")
	saw = Item ("saw","pictures/saw.png")
	MacGuffin = Item ("MacGuffin","pictures/MacGyver.png")
	
	#lists of items and random positions creation 
	#(exept the guardian's position)
	list_items = [burger, hammer, knife, saw, nail, MacGuffin ]
	list_random_position = list(Map.MAP_LABYRINTH)
	list_random_position.remove(Map.MAP_LABYRINTH[-1])
	random.shuffle(list_random_position)
	
	# random positions attribution
	for i in range(len(list_items)):
		item = list_items[i]
		item.position = list_random_position[i]
		item.element_sizing_position()
		print(item.name, "posséde la position  ", item.position)

	return list_items