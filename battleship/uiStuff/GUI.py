import pygame
pygame.init()
from domain.board import *
from domain.boat import *


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
    for i in range(0,BOARD_COL+1):
      for z in range(0,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, (0, 0, 255),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)
    self.createBoatMenu()
    
  def createBoatMenu(self):
    pygame.draw.rect(self.uiInterface,(230,230,230),[0,95,300,500])
    self.boatBattleship.draw()
    self.boatCarrier.draw()
    self.boatDestroyer.draw()
    self.boatSubmarine.draw()
    self.boatPatrol.draw()
    
  def verifyPositionBoat(self,mousePos):
    if self.boatBattleship.position[1] <= mousePos[1] <= (self.boatBattleship.position[1] +self.boatBattleship.height) and self.boatBattleship.position[0] <= mousePos[0] <= (self.boatBattleship.position[0] + self.boatBattleship.width):
      print("Battleship boat")
      rect = self.boatBattleship
    if self.boatCarrier.position[1] <= mousePos[1] <= (self.boatCarrier.position[1] + self.boatCarrier.height) and self.boatCarrier.position[0] <= mousePos[0] <= (self.boatCarrier.position[0] + self.boatCarrier.width):
      print("Carrier boat")
      rect = self.boatCarrier
    if self.boatDestroyer.position[1] <= mousePos[1] <= (self.boatDestroyer.position[1] +self.boatDestroyer.height) and self.boatDestroyer.position[0] <= mousePos[0] <= (self.boatDestroyer.position[0] + self.boatDestroyer.width):
      print("Destroyer boat")
      rect = self.boatDestroyer
    if self.boatSubmarine.position[1] <= mousePos[1] <= (self.boatSubmarine.position[1] +self.boatSubmarine.height) and self.boatSubmarine.position[0] <= mousePos[0] <= (self.boatSubmarine.position[0] + self.boatSubmarine.width):
      print("Submarine boat")
      rect = self.boatSubmarine
    if self.boatPatrol.position[1] <= mousePos[1] <= (self.boatPatrol.position[1] + self.boatPatrol.height) and self.boatPatrol.position[0] <= mousePos[0] <= (self.boatPatrol.position[0] + self.boatPatrol.width):
      print("Patrol boat")
      rect = self.boatPatrol
    return rect

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
      self.boatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,(0,0,0),self.uiInterface)
      self.boatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,(255,0,102),self.uiInterface)
      self.boatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,(100,100,100),self.uiInterface)
      self.boatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,(255,255,0),self.uiInterface)
      self.boatPatrol = Boat('Patrol',BOAT_PATROL,170,375,(51,205,204),self.uiInterface)    
    self.mouseDown = False
    rect = None
    while self.isPlaying:
      self.uiInterface.fill((0,0,0))
      #self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.isPlaying = False
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          # QUIT BUTTON
          if event.button == 1:
            if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
              self.isPlaying = False
              break
            rect = self.verifyPositionBoat(mousePos)
            self.mouseDown = True
          elif event.button == 3:
            self.verifyPositionBoat(mousePos).changeAlign()
        if event.type == pygame.MOUSEBUTTONUP:
          self.mouseDown = False
          rect = None
        if event.type == pygame.MOUSEMOTION and self.mouseDown and rect != None:
          rect.position = mousePos
      self.create_board()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))        
      pygame.display.update() # UPDATE GAME WINDOW
    pygame.quit()
    
      
