from utils.constants import *
from domain.board import *

class Boat:
  
  def __init__(self,name,size,x,y,color,ui,Board,img = '') -> None:
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
    self.img = img
      
  def setImg(self,img):
    self.img = img
    
  def setView(self,view):
    self.view = view
    
  def reInit(self):
    self.position = self.initialPosition
    self.view = None
    self.isAdded = False
    self.boardSquare = (-1,-1)
    self.shots = 0
    
  def setAlign(self,align):
    self.width,self.height = self.height, self.width
    self.align = align
  
  @property
  def getBoardSquare(self):
    return self.boardSquare
  @property
  def getImg(self):
    return self.img
  @property
  def getWidth(self):
    return self.width
  @property
  def getHeight(self):
    return self.height
  @property
  def getColor(self):
    return self.color
  @property
  def getPosition(self):
    return self.position
  @property
  def getAlign(self):
    return self.align
  @property
  def getName(self):
    return self.name
  @property
  def getSunk(self):
    return self.shots == self.size
    
  def setBoardSquare(self,i,z):
    self.boardSquare = (i,z)
    
  def rotateAlign(self):
    if self.getAlign == 'Vertical':
      self.setAlign('Horizontal')
    else:
      self.setAlign('Vertical')
    
  def setBoatSquareSize(self,size):
    if self.width == SQUARE_SIZE or self.width == SQUARE_SIZE_MINI:
      self.width = size
      self.height = self.width * self.size
    else:
      self.height = size
      self.width = self.height * self.size
      
  def __str__(self) -> str:
    return f"{self.name} | {self.position} | {self.boardSquare} | {self.view}"
      
  def __repr__(self) -> str:
    return self.__str__()