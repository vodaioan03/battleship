import pygame
pygame.init()
from domain.board import *


from utils.constants import *


class GUI:
  
  def __init__(self) -> None:
    print("Entry on GUI.")
    
  def playerName(self,playerName):
    self.playerName = playerName

  def mainMenu(self):
    self.uiInterface.fill((0,0,0))
    self.uiInterface.blit(BACKGROUNDIMAGE,(0,0))
    for event in pygame.event.get():  
      if event.type == pygame.QUIT:  
        self.isOnMenu = False
        self.isPlaying = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        #PLAY BUTTON
        if WIDTH/2-80 <= mousePos[0] <= WIDTH/2+48 and HEIGHT/2+50 <= mousePos[1] <= HEIGHT/2+114: 
          self.isOnMenu = False
          self.isPlaying = True
          break
        # QUIT BUTTON
        if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
          self.isOnMenu = False
          self.isPlaying = False
          break
        
    self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-80,HEIGHT/2+50)) 
    self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
    self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
    pygame.display.update() 

  def create_board(self):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, (0, 0, 255),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)

  def startGame(self):
    self.uiInterface = pygame.display.set_mode((WIDTH,HEIGHT))
    self.isPlaying = False
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)
    self.isOnMenu= True
    while self.isOnMenu:
        self.mainMenu()
    if self.isPlaying:
      self.board = Board()    
    
    while self.isPlaying:
      self.uiInterface.fill((0,0,0))
      self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.isPlaying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.isPlaying = False
            break
      self.create_board()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))        
      pygame.display.update() # UPDATE GAME WINDOW
    pygame.quit()
    
      
