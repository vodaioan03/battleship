import pygame

#DISPLAY SETTINGS
WIDTH = 1280
HEIGHT = 720


#colors
COLOR_LIGHT = (170,170,170) 
COLOR_DARK = (100,100,100) 
COLOR_WHITE = (255,255,255)

#FONT
FONT_SIZE = 12
FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)

#IMAGE LOADER
ICON = pygame.image.load('battleship\\utils\\game_logo.jpg')
PLAYBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\play_button.png'),(128,64))
QUITBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\quit_button.png'),(128,64))
BACKGROUNDIMAGE = pygame.transform.scale(pygame.image.load('battleship\\utils\\background_image.jpg'),(WIDTH,HEIGHT))
OCEANBACKGROUND = pygame.transform.scale(pygame.image.load('battleship\\utils\\oceanview.jpg'),(WIDTH,HEIGHT))


#TEXTS
COPYRIGHT = FONT.render('@copyright by Voda',True,COLOR_WHITE)


#BOARD 
BOARD_ROWS = 10
BOARD_COL = 10
SQUARE_SIZE = 55



#BOATS

BOAT_CARRIER = 5  
BOAT_BATTLESHIP = 4
BOAT_DESTROYER = 3
BOAT_SUBMARINE = 3
BOAT_PATROL = 2
