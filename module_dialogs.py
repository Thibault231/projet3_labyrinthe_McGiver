#coding: utf-8
import pygame
from pygame.locals import *

""" 
Module ruling the displays of mac_givers speeches .
"""
def show_dialogs(window_surface):
	""" Display the dialog's box in the main window."""
	dialog_box = pygame.image.load("pictures/dialog_box.png") #  
	dialog_box.convert_alpha()
	# display dialog's box picture in the labyrinth
	window_surface.blit(dialog_box, (0,400))

def picking_speech(speech_index, mac_gyver_counter):
	""" Pick the appropriate speech for the display_speech function."""
	if speech_index == 0:
		text_line1 = ""
		text_line2 = ""
	# speech for finding items
	elif speech_index == 1:
		text_line1 = "I get my {}/5 item.".format(mac_gyver_counter)
		text_line2 = "I'll get out from this hell!"
	# speech for colision with walls
	elif speech_index == 2:
		text_line1 = "I'm not a ghost!"
		text_line2 = "I can't cross the walls."
	# starting speech
	elif speech_index == 3:
		text_line1 = "Where am i?"
		text_line2 = "I have to escape this place."
	return text_line1, text_line2

def show_speech(window_surface, line1, line2):
	""" Display the mac_gyver speech in the dialog box"""
	# Police color
	Blue = (0, 75, 255)
	text_font = pygame.font.SysFont("calibri", 10, True, False )
	#display first speech line
	text_1 = text_font.render(line1,True, Blue)
	window_surface.blit(text_1, [80, 450])
	#display second speech line
	text_2 = text_font.render(line2,True, Blue)
	window_surface.blit(text_2, [80, 460])


def display_speech(speech_index, window_surface, mac_gyver_counter):
	"""  Display a dialog box and an apprpriate mac_gyver's speech."""
	show_dialogs(window_surface)
	line1, line2 = picking_speech(speech_index, mac_gyver_counter)
	show_speech(window_surface, line1, line2)
	pygame.display.flip()

if __name__ == "__main__":
	pygame.init()
	window_resolution = (600, 600)
	pygame.display.set_caption("Labyrinthe Mac Giver")
	window_surface = pygame.display.set_mode(window_resolution, \
	pygame.RESIZABLE)
	display_speech(3, window_surface, 4)

	launched = True
	while launched:
		for event in pygame.event.get():
			# Quit the loop if player close the window
			if event.type == pygame.QUIT:
				launched = False