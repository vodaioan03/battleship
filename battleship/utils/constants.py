import pygame

#DISPLAY SETTINGS
WIDTH = 1280
HEIGHT = 720


#colors
COLOR_LIGHT = (170,170,170) 
COLOR_DARK = (100,100,100) 

#FONT
FONT_SIZE = 12
FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)

#IMAGE LOADER
ICON = pygame.image.load('battleship\\utils\\game_logo.jpg')
PLAYBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\play_button.png'),(128,64))
QUITBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\quit_button.png'),(128,64))
BACKGROUNDIMAGE = pygame.transform.scale(pygame.image.load('battleship\\utils\\background_image.jpg'),(WIDTH,HEIGHT))