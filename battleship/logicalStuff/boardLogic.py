from utils.constants import *
from domain.boat import *
from domain.board import *
import random

class BoardLogic:
  
  def __init__(self) -> None:
    self.boardDomain = Board()
    
  def checkValability(self,boat,align,i,z):
    """Check valability for boat

    Args:
        boat (Boat): boat for check
        align (str): boat align
        i (int): index
        z (int): index

    Returns:
        bool: True or False
    """
    if i == -1 or z == -1:
      return False
    if align == 'Vertical':
      if i+boat.size-1 >= BOARD_COL+1:
        return False
      for k in range(0,boat.size):
        if self.boardDomain.getFromLogicalBoard(i+k,z) != 0:
          return False
    elif align == 'Horizontal':
      if z+boat.size-1 >= BOARD_ROWS+1:
        return False
      for k in range(0,boat.size):
        if self.boardDomain.getFromLogicalBoard(i,z+k) != 0:
          return False
    else:
      return False
    return True
  
  def addToBoard(self,entity,i=-1):
    """Add to board

    Args:
        entity : entity for add
        i (int, optional): index Defaults to -1.
    """
    self.boardDomain.addToBoard(entity,i)
    
  @property
  def emptyBoard(self):
    """Set board to empty
    """
    self.boardDomain.emptyBoard
  @property
  def getBoats(self):
    """Get list with boats

    Returns:
        list: boats
    """
    return self.boardDomain.getBoats
  
  def setBoats(self,boats):
    """Set list with boats

    Args:
        boats (list): list with boats
    """
    self.boardDomain.setBoats(boats)
    
  def verifyCoordsinSquare(self,boat:Boat):
    """Verify coords in square

    Args:
        boat (Boat): boat
    """
    error = False
    i,z = boat.boardSquare[0],boat.boardSquare[1]
    error = self.checkValability(boat,boat.align,i,z)
    error = not error
    if self.boardDomain.getFromLogicalBoard(i,z) == 0 and error == False:
      if boat.align == 'Vertical' and i+boat.size-1 < BOARD_COL+1:
        boat.setBoardSquare(i,z)
        for k in range(0,boat.size):
          self.boardDomain.setValueToLogicalBoard(i+k,z, boat)
          self.boardDomain.addOnes
        boat.isAdded = True
      elif boat.align == 'Horizontal' and z+boat.size-1 < BOARD_ROWS+1:
        boat.setBoardSquare(i,z)
        for k in range(0,boat.size):
          self.boardDomain.setValueToLogicalBoard(i,z+k,boat)
          self.boardDomain.addOnes
        boat.isAdded = True
      else:
        boat.position = boat.initialPosition
        boat.isAdded = False
        boat.setBoardSquare(-1,-1)
    else:
      boat.position = boat.initialPosition
      boat.isAdded = False
      boat.setBoardSquare(-1,-1)
      
  def boatTaken(self,boat:Boat):
    """Call when boat is taken

    Args:
        boat (Boat): boat
    """
    if self.boardDomain.getFromLogicalBoard(boat.boardSquare[0],boat.boardSquare[1]) != 0:
      if boat.align == 'Vertical':
        for k in range(0,boat.size):
          self.boardDomain.setValueToLogicalBoard(boat.boardSquare[0]+k,boat.boardSquare[1],0)
          self.boardDomain.deleteOnes
      elif boat.align == 'Horizontal':
        for k in range(0,boat.size):
          self.boardDomain.setValueToLogicalBoard(boat.boardSquare[0],boat.boardSquare[1]+k,0)
          self.boardDomain.deleteOnes
    boat.setBoardSquare(-1,-1)

      
      
  def boardShot(self,position):
    """Logical for shot

    Args:
        position (tuple): position for boat

    Returns:
        str: message
    """
    message = 'You hit '
    if position[0] > 10 or position[1] > 10:
      position = self.getSquareForCoords(position)
    if position != (-1,-1):
      boatInSquare = self.boardDomain.getFromLogicalBoard(position[0],position[1])
      if boatInSquare != 2:
        if isinstance(boatInSquare,Boat):
          self.boardDomain.addBoatShots(1)
          boatInSquare.shots += 1
          self.lastBoat = boatInSquare
          message += ' a boat!'
          if boatInSquare.getSunk:
            message = f'{boatInSquare.getName} sunk!'
        else:
          message += ' water!'
        self.boardDomain.setValueToLogicalBoard(position[0],position[1],2)
        self.boardDomain.addTotalShots(1)
        self.lastShot = (position[0],position[1])
      else:
        return f"ERROR: Shot {position[0],position[1]} is already added!"
      return message
            
  def createBoats(self):
    """Create boats for user
    """
    self.boatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,COLOR_BLACK,self,IMG_BOAT_CARRIER)
    self.boatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,COLOR_BLACK,self,IMG_BOAT_BATTLESHIP)
    self.boatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,COLOR_BLACK,self,IMG_BOAT_DESTROYER)
    self.boatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,COLOR_BLACK,self,IMG_BOAT_SUBMARINE)
    self.boatPatrol = Boat('Patrol',BOAT_PATROL,170,375,COLOR_BLACK,self,IMG_BOAT_PATROL) 
    
    self.setBoats([self.boatCarrier,self.boatBattleship,self.boatDestroyer,self.boatSubmarine,self.boatPatrol])          
            
  def getBoat(self,name):
    """Search boat for name

    Args:
        name (str): name for boat

    Returns:
        boat: boat
    """
    for each in self.boardDomain.getBoats:
      if each.getName.lower() == name:
        return each
    return None
  
  def getCoords(self,i,z):
    """Get coords for square

    Args:
        i (int): index
        z (int): index

    Returns:
        tuple: coords
    """
    return (self.boardDomain.getFromBoard(i,z,'x'),self.boardDomain.getFromBoard(i,z,'y'))
          
  def getSquareForCoords(self,position):
    """Get square for Coords

    Args:
        position (tuple): tuple with position

    Returns:
        int: position for square
    """
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pos = (self.boardDomain.getFromBoard(i,z,'x'),self.boardDomain.getFromBoard(i,z,'y'))
        if pos[0] <= position[0] and pos[0]+self.boardDomain.getSquareSize > position[0]:
          if pos[1] <= position[1] and pos[1]+self.boardDomain.getSquareSize > position[1]:
            return i,z
    return -1,-1

  
  def checkShoot(self,position):
    """Check if shot is correct or not

    Args:
        position (tuple): square pos

    Returns:
        bool: True or False
    """
    if position[0] > 10 or position[1] > 10:
      position = self.getSquareForCoords(position)
    if position == (-1,-1):
      return False
    if self.boardDomain.getFromLogicalBoard(position[0],position[1]) == 2:
      return False
    return True
  
  def getBoatForCoords(self,x,y):
    """Get boat for a coord

    Args:
        x (int): index
        y (int): index

    Returns:
        Boat: boat
    """
    return self.boardDomain.getFromLogicalBoard(x,y)
  @property
  def readyStart(self):
    """Checks if is ready to start game

    Returns:
        bool: True or False
    """
    return self.boardDomain.getOneNeeded == self.boardDomain.getOnes
  @property
  def getLogicBoard(self):
    """Logic board from domain

    Returns:
        list: logic board
    """
    return self.boardDomain.getLogicBoard
  
  def getCoordsForSquare(self,i,z):
    """Gett coordonates for square

    Args:
        i (int): index
        z (int): index

    Returns:
        tuple: tuple with coords
    """
    return self.boardDomain.getCoordsForSquare(i,z)
  
  def setSquareSize(self,size):
    """Set square size

    Args:
        size (int): square size
    """
    self.boardDomain.setSquareSize(size)
  
  @property
  def verifyWinner(self):
    """Verify winner

    Returns:
        bool: True ig is a winner, else False
    """
    return self.boardDomain.getOneNeeded == self.boardDomain.getBoatShots

  def setWinner(self):
    """Set winner
    """
    self.boardDomain.boatShots = self.boardDomain.getOneNeeded
  
  def verifyPositionBoat(self,mousePos):
    """Verify position if is a boat or not

    Args:
        mousePos (tuple): position for search

    Returns:
        Boat: boat
    """
    for each in self.getBoats:
      if each.position[1] <= mousePos[1] <= (each.position[1] + each.height) and each.position[0] <= mousePos[0] <= (each.position[0] + each.width):
        return each
    return None
  
  def boardReinit(self):
    """Reinit board
    """
    self.boardDomain.clearBoard()
    for each in self.getBoats:
      each.reInit()
      
  def spawnBoat(self,boat:Boat):
    """Spawn boat random

    Args:
        boat (Boat): boat for spawn

    Returns:
        bool: True if boat spawned or false
    """
    square = (-1,-1)
    if self.boardDomain.getBoard != [[]]:
      positionRandom = (random.randint(SQUARE_SIZE+340,SQUARE_SIZE*10+340), random.randint(SQUARE_SIZE+40,SQUARE_SIZE*10+40))
      square = self.getSquareForCoords(positionRandom)
    else:
      square = (random.randint(1,10),random.randint(1,10))
    if self.checkValability(boat,boat.align,square[0],square[1]):
      boat.setBoardSquare(square[0],square[1])
      if self.boardDomain.getBoard != [[]]:
        boat.position = self.getCoordsForSquare(square[0],square[1])
      self.verifyCoordsinSquare(boat)
      return True
    return False
  
  def sendShot(self):
    """Generate random shot

    Returns:
        tuple: square position
    """
    squarei = random.randint(1,BOARD_ROWS)
    squarez = random.randint(1,BOARD_ROWS)
    while self.boardDomain.getFromLogicalBoard(squarei,squarez) == 2:
      squarei = random.randint(1,BOARD_ROWS)
      squarez = random.randint(1,BOARD_ROWS)
    self.lastShot = (squarei,squarez)
    return (squarei,squarez)
  
  
  def getStats(self):
    """Get stats for user

    Returns:
        tuple: tuple with all informations
    """
    boatShoted = self.boardDomain.getBoatShots
    totalShots = self.boardDomain.getTotalShots
    waterShots = totalShots - boatShoted
    remainingBoats = self.boardDomain.getOneNeeded - boatShoted
    return (totalShots,boatShoted,waterShots,remainingBoats)