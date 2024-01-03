from utils.constants import *
from domain.boat import *
from domain.board import *
import pygame
import random

class BoardLogic:
  
  def __init__(self,ui) -> None:
    self.boardDomain = Board(ui)
    self.uiInterface = ui
    
    
  def boardview(self):
    self.boardDomain.emptyBoard
    for i in range(1,BOARD_COL+1):
      self.boardDomain.addToBoard([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE-1,SQUARE_SIZE-1])
        self.boardDomain.addToBoard(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE)*z+340,(SQUARE_SIZE)*i+40,SQUARE_SIZE,SQUARE_SIZE],1),i)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE+340,SQUARE_SIZE+40,BOARD_COL*SQUARE_SIZE,BOARD_ROWS*SQUARE_SIZE],1)
    
  def boardPlaying(self,xAdd,yAdd,text): 
    self.squareSize = SQUARE_SIZE_MINI
    self.uiInterface.blit(text,(xAdd+SQUARE_SIZE_MINI+40,yAdd))
    self.boardDomain.emptyBoard
    for i in range(1,BOARD_COL+1):
      self.boardDomain.addToBoard([[]])
      for z in range(1,BOARD_ROWS+1):
        pygame.draw.rect(self.uiInterface, COLOR_BLUE,[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI-1,SQUARE_SIZE_MINI-1])
        self.boardDomain.addToBoard(pygame.draw.rect(self.uiInterface,(0,0,0),[(SQUARE_SIZE_MINI)*z+xAdd,(SQUARE_SIZE_MINI)*i+yAdd,SQUARE_SIZE_MINI,SQUARE_SIZE_MINI],1),i)
    pygame.draw.rect(self.uiInterface,(0,0,0),[SQUARE_SIZE_MINI+xAdd,SQUARE_SIZE_MINI+yAdd,BOARD_COL*SQUARE_SIZE_MINI,BOARD_ROWS*SQUARE_SIZE_MINI],1)
    
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
  
  def getCoordsForSquare(self,i,z):
    return self.boardDomain.getCoordsForSquare(i,z)
  
  def setSquareSize(self,size):
    self.boardDomain.setSquareSize(size)
  
  @property
  def verifyWinner(self):
    return self.boardDomain.getOneNeeded == self.boardDomain.getBoatShots
  
  def sendShot(self):
    squarei = random.randint(1,BOARD_ROWS)
    squarez = random.randint(1,BOARD_ROWS)
    while self.boardDomain.getFromLogicalBoard(squarei,squarez) == 2:
      squarei = random.randint(1,BOARD_ROWS)
      squarez = random.randint(1,BOARD_ROWS)

    coords = self.boardDomain.getCoordsForSquare(squarei,squarez)
    return self.boardShot(coords)