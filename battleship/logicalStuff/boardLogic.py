from utils.constants import *
from domain.boat import *
from domain.board import *
import random

class BoardLogic:
  
  def __init__(self,ui) -> None:
    self.boardDomain = Board(ui)
    self.uiInterface = ui
    
  def checkValability(self,boat,align,i,z):
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
    self.boardDomain.addToBoard(entity,i)
    
  @property
  def emptyBoard(self):
    self.boardDomain.emptyBoard
  @property
  def getBoats(self):
    return self.boardDomain.getBoats
  
  def setBoats(self,boats):
    self.boardDomain.setBoats(boats)
    
  def verifyCoordsinSquare(self,boat:Boat):
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

      
      
  def boardShot(self,positiom):
    message = 'You hit '
    if positiom[0] > 10 or positiom[1] > 10:
      positiom = self.getSquareForCoords(positiom)
    if positiom != (-1,-1):
      boatInSquare = self.boardDomain.getFromLogicalBoard(positiom[0],positiom[1])
      if boatInSquare != 2:
        if isinstance(boatInSquare,Boat):
          self.boardDomain.addBoatShots(1)
          boatInSquare.shots += 1
          message += ' a boat!'
        else:
          message += ' water!'
        self.boardDomain.setValueToLogicalBoard(positiom[0],positiom[1],2)
        self.boardDomain.addTotalShots(1)
      else:
        return f"ERROR: Shot {positiom[0],positiom[1]} is already added!"
      return message
            
  def createBoats(self):
    self.boatCarrier = Boat('Carrier',BOAT_CARRIER,10,105,COLOR_BLACK,self.uiInterface,self,IMG_BOAT_CARRIER)
    self.boatBattleship = Boat('Battleship',BOAT_BATTLESHIP,80,105,COLOR_BLACK,self.uiInterface,self,IMG_BOAT_BATTLESHIP)
    self.boatDestroyer = Boat('Destroyer',BOAT_DESTROYER,170,105,COLOR_BLACK,self.uiInterface,self,IMG_BOAT_DESTROYER)
    self.boatSubmarine = Boat('Submarine',BOAT_SUBMARINE,100,375,COLOR_BLACK,self.uiInterface,self,IMG_BOAT_SUBMARINE)
    self.boatPatrol = Boat('Patrol',BOAT_PATROL,170,375,COLOR_BLACK,self.uiInterface,self,IMG_BOAT_PATROL) 
    
    self.boardDomain.setBoats([self.boatCarrier,self.boatBattleship,self.boatDestroyer,self.boatSubmarine,self.boatPatrol])          
            
  def getBoat(self,name):
    for each in self.boardDomain.getBoats:
      if each.getName.lower() == name:
        return each
            
  def addShotsOnMap(self):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        if self.boardDomain.getFromLogicalBoard(i,z) == 2:
          x,y = self.boardDomain.getFromBoard(i,z,'x'),self.boardDomain.getFromBoard(i,z,'y')
          self.uiInterface.blit(EXPLODEICON,(x+5,y+5))
          
  def getSquareForCoords(self,positiom):
    for i in range(1,BOARD_COL+1):
      for z in range(1,BOARD_ROWS+1):
        pos = (self.boardDomain.getFromBoard(i,z,'x'),self.boardDomain.getFromBoard(i,z,'y'))
        if pos[0] <= positiom[0] and pos[0]+self.boardDomain.getSquareSize > positiom[0]:
          if pos[1] <= positiom[1] and pos[1]+self.boardDomain.getSquareSize > positiom[1]:
            return i,z
    return -1,-1

  
  def checkShoot(self,positiom):
    if positiom[0] > 10 or positiom[1] > 10:
      positiom = self.getSquareForCoords(positiom)
    if positiom == (-1,-1):
      return False
    if self.boardDomain.getFromLogicalBoard(positiom[0],positiom[1]) == 2:
      return False
    return True
  @property
  def readyStart(self):
    return self.boardDomain.getOneNeeded == self.boardDomain.getOnes
  @property
  def getLogicBoard(self):
    return self.boardDomain.getLogicBoard
  
  def getCoordsForSquare(self,i,z):
    return self.boardDomain.getCoordsForSquare(i,z)
  
  def setSquareSize(self,size):
    self.boardDomain.setSquareSize(size)
  
  @property
  def verifyWinner(self):
    return self.boardDomain.getOneNeeded == self.boardDomain.getBoatShots
  
  def verifyPositionBoat(self,mousePos):
    for each in self.getBoats:
      if each.position[1] <= mousePos[1] <= (each.position[1] + each.height) and each.position[0] <= mousePos[0] <= (each.position[0] + each.width):
        return each
    return None
  
  def boardReinit(self):
    self.boardDomain.clearBoard()
    for each in self.getBoats:
      each.reInit()
      
  def spawnBoat(self,boat:Boat):
    square = (-1,-1)
    positionRandom = (random.randint(SQUARE_SIZE+340,SQUARE_SIZE*10+340), random.randint(SQUARE_SIZE+40,SQUARE_SIZE*10+40))
    square = self.getSquareForCoords(positionRandom)
    if self.checkValability(boat,boat.align,square[0],square[1]):
      boat.setBoardSquare(square[0],square[1])
      boat.position = self.getCoordsForSquare(square[0],square[1])
      self.verifyCoordsinSquare(boat)
      return True
    return False
  
  def sendShot(self):
    squarei = random.randint(1,BOARD_ROWS)
    squarez = random.randint(1,BOARD_ROWS)
    while self.boardDomain.getFromLogicalBoard(squarei,squarez) == 2:
      squarei = random.randint(1,BOARD_ROWS)
      squarez = random.randint(1,BOARD_ROWS)

    coords = self.boardDomain.getCoordsForSquare(squarei,squarez)
    return self.boardShot(coords)