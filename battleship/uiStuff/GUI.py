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
        self.inStrategy = False
        self.isPlaying = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        #PLAY BUTTON
        if WIDTH/2-80 <= mousePos[0] <= WIDTH/2+48 and HEIGHT/2+50 <= mousePos[1] <= HEIGHT/2+114: 
          self.isOnMenu = False
          self.inStrategy = True
          break
        # QUIT BUTTON
        if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
          self.isOnMenu = False
          self.inStrategy = False
          break
        
    self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-80,HEIGHT/2+50)) 
    self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
    self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
    pygame.display.update() 

  def create_board(self):
    self.board.boardview()
    self.createBoatMenu()
    
  def createBoatMenu(self):
    pygame.draw.rect(self.uiInterface,(230,230,230),[0,95,300,500])
    self.boatBattleship.draw()
    self.boatCarrier.draw()
    self.boatDestroyer.draw()
    self.boatSubmarine.draw()
    self.boatPatrol.draw()
    
  def verifyPositionBoat(self,mousePos):
    rect = None
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
    if rect:
      return rect
    return None
  
  def startGame(self):
    self.uiInterface = pygame.display.set_mode((WIDTH,HEIGHT))
    self.isOnMenu= True
    self.inStrategy = False
    self.isPlaying = False
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)
    
    while self.isOnMenu:
        self.mainMenu()
        
        
    if self.inStrategy:
      self.board = Board(self.uiInterface)
      self.boatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,(0,0,0),self.uiInterface)
      self.boatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,(255,0,102),self.uiInterface)
      self.boatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,(100,100,100),self.uiInterface)
      self.boatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,(255,255,0),self.uiInterface)
      self.boatPatrol = Boat('Patrol',BOAT_PATROL,170,375,(51,205,204),self.uiInterface)    
    self.mouseDown = False
    rect = None
    
    
    while self.inStrategy:
      self.uiInterface.fill((0,0,0))
      #self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.inStrategy = False
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          # QUIT BUTTON
          if event.button == 1:
            if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
              self.inStrategy = False
              break
            #START BUTTON
            if WIDTH/2-100 <= mousePos[0] <= WIDTH/2+28 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16 and self.board.ones == self.board.oneNeeded: 
              self.inStrategy = False
              self.isPlaying = True
              break
            rect = self.verifyPositionBoat(mousePos)
            if rect != None:
              self.board.boatTaken(rect)
            self.mouseDown = True
          elif event.button == 3:
            self.verifyPositionBoat(mousePos).changeAlign()
        if event.type == pygame.MOUSEBUTTONUP:
          if rect != None:
            self.board.verifyCoordsinSquare(rect)
          self.mouseDown = False
          rect = None
        if event.type == pygame.MOUSEMOTION and self.mouseDown and rect != None:
          rect.position = mousePos
      self.create_board()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))  
      if self.board.ones == self.board.oneNeeded:
        self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-100,HEIGHT-80)) 
      pygame.display.update() # UPDATE GAME WINDOW
      
      
    while self.isPlaying:
      self.uiInterface.fill((0,0,0))
      self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.isOnMenu = False
          self.inStrategy = False
          self.isPlaying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.isOnMenu = False
            self.inStrategy = False
            self.isPlaying = False
            break

      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      
      pygame.display.update() #
    pygame.quit()
    
      
