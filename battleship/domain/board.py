from utils.constants import *
from domain.boat import *

class Board:
  
  def __init__(self) -> None:
    self.logicBoard = [[0 for _ in range(BOARD_COL+1)] for _ in range(BOARD_ROWS+1)]
    self.logicBoard[0] = []
    self.board = [[]]
    self.oneNeeded = BOAT_CARRIER + BOAT_BATTLESHIP + BOAT_DESTROYER + BOAT_PATROL + BOAT_SUBMARINE
    self.ones = 0
    self.totalShots = 0
    self.boatShots = 0
    self.squareSize = SQUARE_SIZE
    self.boats = []
    
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
    """Set board empty
    """
    self.board = [[]]
    
  def addToBoard(self,entity,i=-1):
    """Add element to board

    Args:
        entity : what do you wan't to add to the list
        i (int, optional): index for board. Defaults to -1.
    """
    if i != -1:
      self.board[i].append(entity)
    else:
      self.board.append(entity)
      
  def getFromLogicalBoard(self,i,j):
    """Get value from domain

    Args:
        i (int): index
        j (int): index

    Returns:
        elemnt from logicBoard
    """
    return self.logicBoard[i][j]
  
  def getFromBoard(self,i,j,elem = ''):
    """Get element from board

    Args:
        i (int): index
        j (int): index
        elem (str, optional): x or y. Defaults to ''.

    Returns:
        coordonate or boat
    """
    if elem == '':
      return self.board[i][j]
    if elem == 'x':
      return self.board[i][j].x
    if elem == 'y':
      return self.board[i][j].y
    
  @property
  def getSquareSize(self):
    """Get size for square

    Returns:
        int: size of square
    """
    return self.squareSize
  @property
  def getBoats(self):
    """Get list with boats

    Returns:
        list: list with boats_
    """
    return self.boats
  @property
  def getBoard(self):
    """Get Board

    Returns:
        list: board
    """
    return self.board
  @property
  def getTotalShots(self):
    """Get total Shots

    Returns:
        int: total shots
    """
    return self.totalShots
  
  def setBoats(self,boats):
    """Set list with boats

    Args:
        boats (list): list with boats
    """
    self.boats = boats
  
  def setSquareSize(self,size):
    """Set square size

    Args:
        size (int): square size for GUI
    """
    self.squareSize = size
  
  def getCoordsForSquare(self,i,z):
    """Get coords for square

    Args:
        i (int): index
        z (int): index

    Returns:
        tuple: coords
    """
    return (self.board[i][z].x+3,self.board[i][z].y+3)
  @property
  def getOneNeeded(self):
    """Get ones needed

    Returns:
        int: number of ones needed
    """
    return self.oneNeeded
  @property
  def getLogicBoard(self):
    """Get logical board

    Returns:
        list: logical board
    """
    return self.logicBoard
  
  @property
  def getOnes(self):
    """Get number of boats added

    Returns:
        int: number of boats added
    """
    return self.ones
    
  @property
  def getBoatShots(self):
    """Number of boat shots

    Returns:
        int: boats shots
    """
    return self.boatShots
  
  def setValueToLogicalBoard(self,i,j,value):
    """Set value in logcal board

    Args:
        i (int): index
        j (int): index
        value : value for set
    """
    self.logicBoard[i][j] = value
           
  @property
  def addOnes(self):
    """Add one to ones
    """
    self.ones += 1
    
  @property
  def deleteOnes(self):
    """Decrease ones with 1
    """
    self.ones -= 1
    
  def addTotalShots(self,value=-1):
    """Add shots to totalShots

    Args:
        value (int, optional): value to add. Defaults to -1.
    """
    if value != -1:
      self.totalShots += value
    else:
      self.totalShots += 1
      
  def addBoatShots(self,value=-1):
    """Add shots to boats

    Args:
        value (int, optional): shots to add. Defaults to -1.
    """
    if value != -1:
      self.boatShots += value
    else:
      self.boatShots += 1