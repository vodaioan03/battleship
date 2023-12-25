from utils.constants import *
from domain.board import *
import pygame
class Boat:
  
  def __init__(self,name,size,x,y,color,ui,Board) -> None:
    self.name = name 
    self.size = size
    self.initialPosition = (x,y)
    self.position = (x,y)
    self.color = color
    self.uiInterface = ui
    self.view = None
    self.align = 'Vertical'
    self.width = SQUARE_SIZE
    self.height = self.size * self.width
    self.isAdded = False
    self.boardSquare = (-1,-1)
    self.board = Board
    self.shots = 0
    
  def changeAlign(self):
    if not self.isAdded:
      self.width,self.height = self.height, self.width
      if self.align == 'Vertical':
        self.align = 'Horizontal'
      else:
        self.align = 'Vertical'
    else:
      pass
    
  def draw(self):
    x = y = None
    if self.boardSquare[0] != -1:
      boatRect = self.board.board[self.boardSquare[0]][self.boardSquare[1]]
      x=boatRect.x
      y=boatRect.y
    if x != None:
      self.view = pygame.draw.rect(self.uiInterface,self.color,[x,y,self.width,self.height])
    else:
      self.view = pygame.draw.rect(self.uiInterface,self.color,[self.position[0],self.position[1],self.width,self.height])
    
  def setBoardSquare(self,i,z):
    self.boardSquare = (i,z)
    print(self.boardSquare)
    
  def setSquareSize(self,size):
    if self.width == SQUARE_SIZE:
      self.width = SQUARE_SIZE_MINI
      self.height = self.width * self.size
    else:
      self.height = SQUARE_SIZE_MINI
      self.width = self.height * self.size
      
  def __str__(self) -> str:
    return f"{self.name} | {self.position} | {self.boardSquare} | {self.view}"
      
  def __repr__(self) -> str:
    return self.__str__()