import random
import pygame
pygame.init()
from domain.board import *
from domain.boat import *


from utils.constants import *


class GUI:
  
  def __init__(self) -> None:
    print("Entry on GUI.")
    self.playerBoats = []
    self.computerBoats = []
    self.winner = None
    
  def playerName(self,playerName):
    self.playerName = playerName
    
  
  def createBoatsForComputer(self):
    for each in self.computerBoats:
      while each.boardSquare[0] == -1:
        number = random.randint(1,100)
        if number % 2 == 0:
          each.changeAlign()
        each.position = (random.randint(SQUARE_SIZE+340,SQUARE_SIZE*10+340), random.randint(SQUARE_SIZE+40,SQUARE_SIZE*10+40))
        each.draw()
        self.computerBoard.verifyCoordsinSquare(each)
    
    
    
  #MAIN MENU 
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
    
    
  #STRATEGY PANEL
  def strategyPanel(self):
    self.uiInterface.fill((0,0,0))
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
          if WIDTH/2-100 <= mousePos[0] <= WIDTH/2+28 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16 and self.playerBoard.ones == self.playerBoard.oneNeeded: 
            self.inStrategy = False
            self.isPlaying = True
            break
          self.rect = self.verifyPositionBoat(mousePos)
          if self.rect != None:
            self.playerBoard.boatTaken(self.rect)
          self.mouseDown = True
        elif event.button == 3:
          self.rect = self.verifyPositionBoat(mousePos)
          if self.rect != None and self.rect.isAdded != True:
            self.rect.changeAlign()
          else:
            self.rect = None
      if event.type == pygame.MOUSEBUTTONUP:
        if self.rect != None:
          self.playerBoard.verifyCoordsinSquare(self.rect)
        self.mouseDown = False
        self.rect = None
      if event.type == pygame.MOUSEMOTION and self.mouseDown and self.rect != None:
        self.rect.position = mousePos
    self.create_board()
    self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
    self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))  
    self.uiInterface.blit(STRATEGY_PANEL,(WIDTH/2-120,50))
    if self.playerBoard.ones == self.playerBoard.oneNeeded:
      self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-100,HEIGHT-80)) 
    pygame.display.update() # UPDATE GAME WINDOW
    
    
    
  def playingPanel(self):
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
          self.inWinner = False
          break
        if SQUARE_SIZE_MINI+80 <= mousePos[0] <= SQUARE_SIZE_MINI*(BOARD_ROWS+1)+80 and SQUARE_SIZE_MINI+150 <= mousePos[1] <= SQUARE_SIZE_MINI*(BOARD_COL+1)+150:
          print("pe buton : ",mousePos)
          self.computerBoard.boardShot(mousePos)
    self.playerBoard.boardPlaying(700,150,PLAYER_BOARD)
    self.computerBoard.boardPlaying(80,150,COMPUTER_BOARD)
    self.createBoatsView()
    self.createComputerBoatsView()
    self.computerBoard.addShotsOnMap()
    self.playerBoard.addShotsOnMap()
    self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
    self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))

    if self.computerBoard.boatShots == self.computerBoard.oneNeeded:
      self.winner = 1
    elif self.playerBoard.boatShots == self.playerBoard.oneNeeded:
      self.winner = 2
    
    if self.winner != None:
      self.isPlaying = False
      self.inWinner = True
    
    pygame.display.update() #
      
      
  def winnerPanel(self):
    self.uiInterface.fill((0,0,0))
    
    for event in pygame.event.get():  
      if event.type == pygame.QUIT:  
        self.isOnMenu = False
        self.inStrategy = False
        self.isPlaying = False
        self.inWinner = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        # QUIT BUTTON
        if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
          self.isOnMenu = False
          self.inStrategy = False
          self.isPlaying = False
          self.inWinner = False
          break
    self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
    self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))

    
    pygame.display.update() #

    
    
  def create_board(self):
    self.playerBoard.boardview()
    pygame.draw.rect(self.uiInterface,(230,230,230),[0,95,300,500])
    self.createBoatsView()
    
  def createBoatsView(self):
    for each in self.playerBoats:
      each.draw()
  
  def createComputerBoatsView(self):
    for each in self.computerBoats:
      each.draw()
    
  def createBoats(self):
    self.playerBoard = Board(self.uiInterface)
    self.boatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,(0,0,0),self.uiInterface,self.playerBoard)
    self.boatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,(255,0,102),self.uiInterface,self.playerBoard)
    self.boatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,(100,100,100),self.uiInterface,self.playerBoard)
    self.boatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,(255,255,0),self.uiInterface,self.playerBoard)
    self.boatPatrol = Boat('Patrol',BOAT_PATROL,170,375,(51,205,204),self.uiInterface,self.playerBoard) 
    
    self.playerBoats = [self.boatCarrier,self.boatBattleship,self.boatDestroyer,self.boatSubmarine,self.boatPatrol]
    
    self.computerBoard = Board(self.uiInterface)
    self.computerBoatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,(0,0,0),self.uiInterface,self.computerBoard)
    self.computerBoatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,(255,0,102),self.uiInterface,self.computerBoard)
    self.computerBoatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,(100,100,100),self.uiInterface,self.computerBoard)
    self.computerBoatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,(255,255,0),self.uiInterface,self.computerBoard)
    self.computerBoatPatrol = Boat('Patrol',BOAT_PATROL,170,375,(51,205,204),self.uiInterface,self.computerBoard) 
    
    self.computerBoats = [self.computerBoatCarrier,self.computerBoatBattleship,self.computerBoatDestroyer,self.computerBoatSubmarine,self.computerBoatPatrol]
    
    
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
    self.inWinner = False
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)
    
    while self.isOnMenu:
        self.mainMenu()
        
        
    if self.inStrategy:
      self.createBoats()  
       
    self.mouseDown = False
    
    self.rect = None
    # STRATEGY PANEL
    while self.inStrategy:
      self.strategyPanel()
      
    if self.isPlaying:
      self.computerBoard.boardview()
      self.createBoatsForComputer()
      
      for each in self.computerBoats:
        print(each)
      
      for each in self.playerBoats:
        each.setSquareSize(SQUARE_SIZE_MINI)
      for each in self.computerBoats:
        each.setSquareSize(SQUARE_SIZE_MINI)
      
    while self.isPlaying:
      self.playingPanel()
      
    while self.inWinner:
      self.winnerPanel()
      
    pygame.quit()