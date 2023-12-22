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
    print(self.oneNeeded)
    self.ones = 0
      
  def boardview(self):
    for i in range(1,BOARD_COL+1):
      self.board.append([])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, (0, 0, 255),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        self.board[i].append(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1))
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)
    
  def verifyCoordsinSquare(self,boat:Boat):
    found = False
    error = False
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if boat.view.colliderect(self.board[i][z]):
          boat.position = (self.board[i][z].x,self.board[i][z].y)
          if self.logicBoard[i][z] == 0:
            if boat.align == 'Vertical' and i+boat.size < BOARD_COL+1:
              print("Vertical")
              for k in range(0,boat.size):
                print(i,z)
                if self.logicBoard[i+k][z] == 1:
                  error = True
                  found = True
                  break
                self.logicBoard[i+k][z] = 1
                self.ones += 1
              boat.isAdded = True
            elif boat.align == 'Horizontal' and z+boat.size < BOARD_ROWS+1:
              print("Horizontal")
              for k in range(0,boat.size):
                if self.logicBoard[i][z+k] == 1:
                  error = True
                  found = True
                  break
                self.logicBoard[i][z+k] = 1
                self.ones += 1
              boat.isAdded = True
            else:
              boat.position = boat.initialPosition
              boat.isAdded = False
          else:
            boat.position = boat.initialPosition
            boat.isAdded = False
          found = True
          for k in range(len(self.logicBoard)):
            print(self.logicBoard[k])
          break
      if error:
        boat.position = boat.initialPosition
        boat.isAdded = False
      if found:
        break
      
  def boatTaken(self,boat:Boat):
    found = False
    print(boat.position)
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if boat.view.colliderect(self.board[i][z]):
          boat.position = (self.board[i][z].x,self.board[i][z].y)
          if self.logicBoard[i][z] == 1:
            if boat.align == 'Vertical':
              for k in range(0,boat.size):
                self.logicBoard[i+k][z] = 0
                self.ones -= 1
            elif boat.align == 'Horizontal':
              for k in range(0,boat.size):
                self.logicBoard[i][z+k] = 0
                self.ones -= 1
          found = True
          for k in range(len(self.logicBoard)):
            print(self.logicBoard[k])
          break
      if found:
        break