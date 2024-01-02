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
    
  def clearBoard(self):
    self.logicBoard = [[0 for _ in range(BOARD_COL+1)] for _ in range(BOARD_ROWS+1)]
    self.logicBoard[0] = []
    self.board = [[]]
    self.oneNeeded = BOAT_CARRIER + BOAT_BATTLESHIP + BOAT_DESTROYER + BOAT_PATROL + BOAT_SUBMARINE
    self.ones = 0
    self.totalShots = 0
    self.boatShots = 0
    
  @property
  def emptyBoard(self):
    self.board = [[]]
    
  def addToBoard(self,entity,i=-1):
    if i != -1:
      self.board[i].append(entity)
    else:
      self.board.append(entity)
      
  def getFromLogicalBoard(self,i,j):
    return self.logicBoard[i][j]
  
  def getFromBoard(self,i,j,elem = ''):
    if elem == '':
      return self.board[i][j]
    if elem == 'x':
      return self.board[i][j].x
    if elem == 'y':
      return self.board[i][j].y
    
  @property
  def getSquareSize(self):
    return self.squareSize
  
  def setSquareSize(self,size):
    self.squareSize = size
  
  def getCoordsForSquare(self,i,z):
    return (self.board[i][z].x+3,self.board[i][z].y+3)
  @property
  def getOneNeeded(self):
    return self.oneNeeded
  
  @property
  def getOnes(self):
    return self.ones
    
  @property
  def getBoatShots(self):
    return self.boatShots
  
  def setValueToLogicalBoard(self,i,j,value):
    self.logicBoard[i][j] = value
           
  @property
  def addOnes(self):
    self.ones += 1
    
  def addTotalShots(self,value=-1):
    if value != -1:
      self.totalShots += value
    else:
      self.totalShots += 1
      
  def addBoatShots(self,value=-1):
    if value != -1:
      self.boatShots += value
    else:
      self.boatShots += 1