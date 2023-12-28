from utils.constants import *
from domain.boat import *
import pygame
class Board:
  
  def __init__(self,ui) -> None:
    print("Init board")
    self.logicBoard = [[0 for _ in range(BOARD_COL+1)] for _ in range(BOARD_ROWS+1)]
    self.logicBoard[0] = []
    self.board = [[]]
    self.uiInterface = ui
    self.oneNeeded = BOAT_CARRIER + BOAT_BATTLESHIP + BOAT_DESTROYER + BOAT_PATROL + BOAT_SUBMARINE
    self.ones = 0
    self.totalShots = 0
    self.boatShots = 0
    self.squareSize = SQUARE_SIZE
      
  def boardview(self):
    self.board  = [[]]
    for i in range(1,BOARD_COL+1):
      self.board.append([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        self.board[i].append(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1))
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)
    
  def boardPlaying(self,xAdd,yAdd,text): 
    self.squareSize = SQUARE_SIZE_MINI
    self.uiInterface.blit(text,(xAdd+SQUARE_SIZE_MINI+40,yAdd))
    self.board  = [[]]
    for i in range(1,BOARD_COL+1):
      self.board.append([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI-1,SQUARE_SIZE_MINI-1])
        self.board[i].append(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI,SQUARE_SIZE_MINI],1))
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE_MINI+xAdd,SQUARE_SIZE_MINI+yAdd,BOARD_COL*SQUARE_SIZE_MINI,BOARD_ROWS*SQUARE_SIZE_MINI],1)
    
  def verifyCoordsinSquare(self,boat:Boat):
    found = False
    error = False
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if boat.view.colliderect(self.board[i][z]):
          boat.position = (self.board[i][z].x,self.board[i][z].y)
          if self.logicBoard[i][z] == 0:
            if boat.align == 'Vertical' and i+boat.size-1 < BOARD_COL+1:
              for k in range(0,boat.size):
                if self.logicBoard[i+k][z] != 0:
                  error = True
                  found = True
                  break
              if error == False:
                for k in range(0,boat.size):
                  if self.logicBoard[i+k][z] != 0:
                    error = True
                    found = True
                    break
                  self.logicBoard[i+k][z] = boat
                  self.ones += 1
              boat.isAdded = True
              boat.setBoardSquare(i,z)
            elif boat.align == 'Horizontal' and z+boat.size-1 < BOARD_ROWS+1:
              for k in range(0,boat.size):
                if self.logicBoard[i][z+k] != 0:
                  error = True
                  found = True
                  break
              if error == False:
                for k in range(0,boat.size):
                  if self.logicBoard[i][z+k] != 0:
                    error = True
                    found = True
                    break
                  self.logicBoard[i][z+k] = boat
                  self.ones += 1
              boat.isAdded = True
              boat.setBoardSquare(i,z)
            else:
              boat.position = boat.initialPosition
              boat.isAdded = False
              boat.setBoardSquare(-1,-1)
          else:
            boat.position = boat.initialPosition
            boat.isAdded = False
            boat.setBoardSquare(-1,-1)
          found = True
          break
      if error:
        boat.position = boat.initialPosition
        boat.isAdded = False
        boat.setBoardSquare(-1,-1)
      if found:
        break
      
  def boatTaken(self,boat:Boat):
    found = False
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if boat.view.colliderect(self.board[i][z]):
          boat.position = (self.board[i][z].x,self.board[i][z].y)
          if self.logicBoard[i][z] != 0:
            if boat.align == 'Vertical':
              for k in range(0,boat.size):
                self.logicBoard[i+k][z] = 0
                self.ones -= 1
            elif boat.align == 'Horizontal':
              for k in range(0,boat.size):
                self.logicBoard[i][z+k] = 0
                self.ones -= 1
          found = True
          break
      if found:
        boat.setBoardSquare(-1,-1)
        break
      
      
  def boardShot(self,positiom):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pos = (self.board[i][z].x,self.board[i][z].y)
        if pos[0] < positiom[0] and pos[0]+self.squareSize >= positiom[0]:
          if pos[1] < positiom[1] and pos[1]+self.squareSize >= positiom[1]:
            boatInSquare = self.logicBoard[i][z]
            if boatInSquare != 2:
              if isinstance(boatInSquare,Boat):
                self.boatShots += 1
                boatInSquare.shots += 1
              self.logicBoard[i][z] = 2
              self.totalShots += 1
            else:
              print(f"ERROR: Shot {i,z} is already added!")
              return
            
  def addShotsOnMap(self):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if self.logicBoard[i][z] == 2:
          x,y = self.board[i][z].x,self.board[i][z].y
          self.uiInterface.blit(EXPLODEICON,(x+5,y+5))
          
          
          
  def getSquareForCoords(self,positiom):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pos = (self.board[i][z].x,self.board[i][z].y)
        if pos[0] < positiom[0] and pos[0]+self.squareSize >= positiom[0]:
          if pos[1] < positiom[1] and pos[1]+self.squareSize >= positiom[1]:
            return i,z
    return -1,-1
  
  def getCoordsForSquare(self,i,z):
    return (self.board[i][z].x+3,self.board[i][z].y+3)
  
  def checkShoot(self,positiom):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pos = (self.board[i][z].x,self.board[i][z].y)
        if pos[0] < positiom[0] and pos[0]+self.squareSize >= positiom[0]:
          if pos[1] < positiom[1] and pos[1]+self.squareSize >= positiom[1]:
            if self.logicBoard[i][z] == 2:
              return False
    return True
           