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
class Item(Element):
	"""
	Define a children class for all items which should 
	be collected by Mac Giver.
	"""