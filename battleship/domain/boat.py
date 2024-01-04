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
    """Set img for GUI

    Args:
        img (pygame): image
    """
    self.img = img
    
  def setView(self,view):
    """Set biew for GUI

    Args:
        view (pygame): rect
    """
    self.view = view
    
  def reInit(self):
    """Re init all values
    """
    self.position = self.initialPosition
    self.view = None
    self.isAdded = False
    self.boardSquare = (-1,-1)
    self.shots = 0
    
  def setAlign(self,align):
    """Set align for boat

    Args:
        align (str): align Vertical or Horizontal
    """
    self.width,self.height = self.height, self.width
    self.align = align
  
  @property
  def getBoardSquare(self):
    """Get board square

    Returns:
        tuple: board square
    """
    return self.boardSquare
  @property
  def getImg(self):
    """Get img 

    Returns:
        pygame: image
    """
    return self.img
  @property
  def getWidth(self):
    """Get width

    Returns:
        int: width
    """
    return self.width
  @property
  def getHeight(self):
    """Get height

    Returns:
        int: height
    """
    return self.height
  @property
  def getColor(self):
    """Get color

    Returns:
        tuple: color
    """
    return self.color
  @property
  def getPosition(self):
    """Get position

    Returns:
        tuple: get position
    """
    return self.position
  @property
  def getAlign(self):
    """Get align

    Returns:
        str: align
    """
    return self.align
  @property
  def getName(self):
    """Get boat name

    Returns:
        str: boat name
    """
    return self.name
  @property
  def getSize(self):
    """Get boat size

    Returns:
        int: boat size
    """
    return self.size
  @property
  def getSunk(self):
    """Get if boat is stunk or not

    Returns:
        bool: True if stunks, false else
    """
    return self.shots == self.size
    
  def setBoardSquare(self,i,z):
    """Get board square

    Args:
        i (int): index
        z (int): index
    """
    self.boardSquare = (i,z)
    
  def rotateAlign(self):
    """Rotate align
    """
    if self.getAlign == 'Vertical':
      self.setAlign('Horizontal')
    else:
      self.setAlign('Vertical')
    
  def setBoatSquareSize(self,size):
    """Set boat square size

    Args:
        size (int): square size
    """
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