import pygame
pygame.init()

from utils.constants import *


class GUI:
  
  def __init__(self) -> None:
    print("Entry on GUI.")

  def startGame(self):
    self.uiInterface = pygame.display.set_mode((WIDTH,HEIGHT))
    self.isPlaying = False
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)
    isOnMenu = True
    while isOnMenu:
        self.uiInterface.fill((0,0,0))
        self.uiInterface.blit(BACKGROUNDIMAGE,(0,0))
        for event in pygame.event.get():  
          if event.type == pygame.QUIT:  
            isOnMenu = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            #PLAY BUTTON
            if WIDTH/2-80 <= mousePos[0] <= WIDTH/2+48 and HEIGHT/2+50 <= mousePos[1] <= HEIGHT/2+114: 
              isOnMenu = False
              isPlaying = True
              break
            # QUIT BUTTON
            if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
              isOnMenu = False
              isPlaying = False
              break
            
        self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-80,HEIGHT/2+50)) 
        self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
        pygame.display.update() 
        
    while isPlaying:
      self.uiInterface.fill((0,0,0))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          isPlaying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
              
      pygame.display.update()
      # updates the frames of the game 
    pygame.quit()
      
