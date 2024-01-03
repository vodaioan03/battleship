import random
import time
import pygame
pygame.init()
from logicalStuff.boardLogic import *
from domain.boat import *
from utils.constants import *

class GUI:
  
  def __init__(self) -> None:
    self.isOnMenu= True
    self.inStrategy = False
    self.isPlaying = False
    self.inWinner = False
    self.mouseDown = False
    self.rect = None
    self.turn = 'Player'
    self.winner = None
    self.debug = False
    self.message = ''
    
  def addBoards(self):
    self.playerBoard = BoardLogic(self.uiInterface)
    self.computerBoard = BoardLogic(self.uiInterface)
    
  def playerName(self,playerName):
    self.playerName = playerName
    
  def quitGame(self):
    self.isOnMenu= False
    self.inStrategy = False
    self.isPlaying = False
    self.inWinner = False
    
  def spawnRandomBoats(self, boardUse:Board,boats:list):
    boardUse.boardReinit()
    for each in boats:
      if each.getAlign == 'Horizontal':
        self.changeAlign(each)
        each.setAlign('Vertical')
    self.boardview(boardUse)
    for boat in boats:
      added = False
      while not added:
        number = random.randint(1,100)
        if number % 2 == 0:
          self.changeAlign(boat)
          if boat.getAlign == 'Horizontal':
            boat.setAlign('Vertical')
          else:
            boat.setAlign('Horizontal')
        added = boardUse.spawnBoat(boat)
      
  def changeAlign(self,boat:Boat):
    if not boat.isAdded:
      if boat.align == 'Vertical':
        boat.setImg(pygame.transform.rotate(boat.img, 90))
      else:
        boat.setImg(pygame.transform.rotate(boat.img, -90))
    else:
      print("Boatt already added!")
    
    
  #MAIN MENU 
  def mainMenu(self):
    while self.isOnMenu:
      self.uiInterface.fill(COLOR_BLACK)
      self.uiInterface.blit(BACKGROUNDIMAGE,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          
          #PLAY BUTTON
          if WIDTH/2-80 <= mousePos[0] <= WIDTH/2+48 and HEIGHT/2+50 <= mousePos[1] <= HEIGHT/2+114: 
            self.isOnMenu = False
            self.inStrategy = True
            break
          
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
          
      self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-80,HEIGHT/2+50)) 
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      pygame.display.update() 
    
    
  #STRATEGY PANEL
  def strategyPanel(self):
    if self.inStrategy:
      self.createBoats() 
      
    while self.inStrategy:
      self.uiInterface.fill(COLOR_BLACK)
      self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          
          if event.button == 1:
            
            # QUIT BUTTON
            if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
              self.quitGame()
              break
            
            #START BUTTON
            if WIDTH/2-100 <= mousePos[0] <= WIDTH/2+28 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16 and self.playerBoard.readyStart: 
              self.inStrategy = False
              self.isPlaying = True
              break
            
            #SHUFFLE BUTTON
            if 130 <= mousePos[0] <= 180 and HEIGHT-120 <= mousePos[1] <= HEIGHT-70: 
              self.spawnRandomBoats(self.playerBoard,self.playerBoard.getBoats)
            self.rect = self.playerBoard.verifyPositionBoat(mousePos)
            
            if self.rect != None:
              self.playerBoard.boatTaken(self.rect)
            self.mouseDown = True
          elif event.button == 3:
            self.rect = self.playerBoard.verifyPositionBoat(mousePos)
            if self.rect != None and self.rect.isAdded != True:
              self.changeAlign(self.rect)
              if self.rect.getAlign == 'Vertical':
                self.rect.setAlign('Horizontal')
              else:
                self.rect.setAlign('Vertical')
            else:
              self.rect = None
        if event.type == pygame.MOUSEBUTTONUP:
          if self.rect != None and self.mouseDown == True:
            boat = self.rect
            square = self.playerBoard.getSquareForCoords(mousePos)
            if self.playerBoard.checkValability(boat,boat.align,square[0],square[1]):
              boat.boardSquare = square
              boat.position = self.playerBoard.getCoordsForSquare(square[0],square[1])
              self.playerBoard.verifyCoordsinSquare(boat)
            else:
              boat.reInit()
              if boat.getAlign == 'Horizontal':
                self.changeAlign(boat)
                boat.setAlign('Vertical')
          self.mouseDown = False
          self.rect = None
        if event.type == pygame.MOUSEMOTION and self.mouseDown and self.rect != None:
          self.rect.position = mousePos
            
      self.create_board()
      
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))  
      self.uiInterface.blit(STRATEGY_PANEL,(WIDTH/2-120,50))
      self.uiInterface.blit(SHUFFLE_BUTTON,(130,HEIGHT-120))
      
      if self.playerBoard.readyStart:
        self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-100,HEIGHT-80)) 
      pygame.display.update() # UPDATE GAME WINDOW
    
  def draw(self,boardUse, boat:Boat):
    x = y = None
    boardSquare = boat.getBoardSquare
    position = boat.getPosition
    if boardSquare[0] != -1:
      boatRect = boardUse.boardDomain.getFromBoard(boardSquare[0],boardSquare[1])
      x=boatRect.x
      y=boatRect.y
    if x != None:
      boat.setView(pygame.draw.rect(self.uiInterface,boat.getColor,[x,y,boat.getWidth,boat.getHeight],1))
      self.uiInterface.blit(boat.getImg,(x,y))
    else:
      boat.setView(pygame.draw.rect(self.uiInterface,boat.getColor,[position[0],position[1],boat.getWidth,boat.getHeight],1))
      self.uiInterface.blit(boat.getImg,(position[0],position[1]))
  
  def changeSquareSize(self,boat:Boat,squareSize):
    boat.setBoatSquareSize(squareSize)
    boat.setImg(pygame.transform.scale(boat.getImg,(boat.getWidth,boat.getHeight)))
    
  def playingPanel(self):
    if self.isPlaying:
      self.boardview(self.computerBoard)
      self.spawnRandomBoats(self.computerBoard,self.computerBoard.getBoats)
      
      self.playerBoard.setSquareSize(SQUARE_SIZE_MINI)
      self.computerBoard.setSquareSize(SQUARE_SIZE_MINI)
      
      for each in self.playerBoard.getBoats:
        self.changeSquareSize(each,SQUARE_SIZE_MINI)
      for each in self.computerBoard.getBoats:
        self.changeSquareSize(each,SQUARE_SIZE_MINI)
    while self.isPlaying:
      self.uiInterface.fill(COLOR_BLACK)
      self.uiInterface.blit(OCEAN_STORM,(0,0))
      
      if self.turn == 'Computer':
        self.uiInterface.blit(self.message,(120+SQUARE_SIZE_MINI+40,600))
        self.endtime = time.time()
        if self.endtime - self.start_time > 2:
          self.message = self.playerBoard.sendShot()
          self.message = BIG_FONT.render(self.message,True,COLOR_WHITE)
          self.turn = 'Player'
      if self.turn == 'Player' and self.message != '':
        self.uiInterface.blit(self.message,(740+SQUARE_SIZE_MINI+40,600))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
          if self.turn == 'Player':
            if SQUARE_SIZE_MINI+80 <= mousePos[0] <= SQUARE_SIZE_MINI*(BOARD_ROWS+1)+80 and SQUARE_SIZE_MINI+150 <= mousePos[1] <= SQUARE_SIZE_MINI*(BOARD_COL+1)+150:
              if self.computerBoard.checkShoot(mousePos):
                self.message = self.computerBoard.boardShot(mousePos)
                self.message = BIG_FONT.render(self.message,True,COLOR_WHITE)
                self.turn = 'Computer'
                self.start_time = time.time()
              else:
                print("Invalid Shot!")
          else:
            print("Isn't your turn.")
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_F1:
            self.debug = not self.debug
          if self.debug:
            if event.key == pygame.K_F2:
              self.winner = 2
              
      #CREATE EMPTY BOARD
      self.boardPlaying(self.playerBoard,700,150,PLAYER_BOARD)
      self.boardPlaying(self.computerBoard,80,150,COMPUTER_BOARD)
      
      #CREATE VIEW BOATS
      self.createBoatsView()
      if self.debug:
        self.createComputerBoatsView()
        
      #ADD SHOTS ON THE BOARD
      self.computerBoard.addShotsOnMap()
      self.playerBoard.addShotsOnMap()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      
      pygame.display.update() #
      
      if self.computerBoard.verifyWinner:
        self.winner = 1 #PLAYER
      elif self.playerBoard.verifyWinner:
        self.winner = 2 #COMPUTER
      
      if self.winner != None:
        self.isPlaying = False
        self.inWinner = True
      
      
  def winnerPanel(self):
    while self.inWinner:
      self.uiInterface.fill((100,100,100))
      self.uiInterface.blit(WINNERBACKGROUND,(0,0))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      if self.winner == 1:
        self.uiInterface.blit(WIN,(450,150))
      else:
        self.uiInterface.blit(LOOSE,(450,150))
      
      pygame.display.update() #
    
  def create_board(self):
    self.boardview(self.playerBoard)
    self.uiInterface.blit(TEXTURE,(0,95))
    self.createBoatsView()
    
  def createBoatsView(self):
    for each in self.playerBoard.getBoats:
      self.draw(self.playerBoard,each)
  
  def createComputerBoatsView(self):
    for each in self.computerBoard.getBoats:
      self.draw(self.computerBoard,each)
  
  def createBoats(self):
    self.createPlayerBoats()
    self.createComputerBoats()
    
  def createPlayerBoats(self):
    self.playerBoard.createBoats()
    self.setImagesBoats(self.playerBoard.getBoats)
  
  def createComputerBoats(self):
    self.computerBoard.createBoats()
    
    self.setImagesBoats(self.computerBoard.getBoats)
    
  def setImagesBoats(self,boats:list):
    for each in boats:
      each.setImg(pygame.transform.scale(each.getImg,(each.getWidth,each.getHeight)))
  
  
  def boardview(self,boardUse:Board):
    boardUse.emptyBoard
    for i in range(1,BOARD_COL+1):
      boardUse.addToBoard([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        boardUse.addToBoard(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1),i)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)
    
  def boardPlaying(self,boardUse:Board,xAdd,yAdd,text): 
    boardUse.setSquareSize(SQUARE_SIZE_MINI)
    self.uiInterface.blit(text,(xAdd+SQUARE_SIZE_MINI+40,yAdd))
    boardUse.emptyBoard
    for i in range(1,BOARD_COL+1):
      boardUse.addToBoard([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI-1,SQUARE_SIZE_MINI-1])
        boardUse.addToBoard(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI,SQUARE_SIZE_MINI],1),i)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE_MINI+xAdd,SQUARE_SIZE_MINI+yAdd,BOARD_COL*SQUARE_SIZE_MINI,BOARD_ROWS*SQUARE_SIZE_MINI],1)
  
  
  
  def startGame(self):
    self.uiInterface = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)
    self.addBoards()

    #MAIN MENU
    self.mainMenu()
    # STRATEGY PANEL
    self.strategyPanel()
    # PLAYING PANEL
    self.playingPanel()
    # WINNER PANEL
    self.winnerPanel()
    
    pygame.quit()