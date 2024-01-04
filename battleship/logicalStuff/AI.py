from utils.constants import *
from domain.boat import *
from domain.board import *
from logicalStuff.boardLogic import *
import random
import copy


class AI:
  
  def __init__(self,board:Board) -> None:
    self.board = board
    self.boats = copy.copy(self.board.getBoats)
    self.aligns = [' ' for _ in range(len(self.boats))]
    self.positions = {} # {'':N- i-1,S- i+1,V- j-1,E- j+1}
    
  def deleteSunk(self,boat):
    """Delete a boat what is sunk

    Args:
        boat (Boat): boat for delete
    """
    for i in range(len(self.boats)):
      if self.boats[i] == boat:
        self.boats.remove(boat)
        break
    
  def addPosition(self,square):
    """Add position to list

    Args:
        square (tuple): square position
    """
    self.positions[f'{square[0]},{square[1]}'] = [(-1,0),(1,0),(0,-1),(0,1)]

    
  def deleteFromPosition(self,square,index):
    """Delete from position

    Args:
        square (tuple): square position
        index (int): index for delete
    """
    self.positions[f'{square[0]},{square[1]}'][index] = (0,0)
    self.deletePosition(square)
    
    
    
  def deletePosition(self,square):
    """Delete from position list

    Args:
        square (tuple): square position
    """
    delete = True
    for each in self.positions[f'{square[0]},{square[1]}']:
      if each != (0,0):
        delete = False
    if delete == True:
      del self.positions[f'{square[0]},{square[1]}']
      
  def findTheLargestBoat(self):
    """Find the smaller boat from list with active boats

    Returns:
        Boat: boat object
    """
    maximum = 7
    boat = ''
    for each in self.boats:
      if each.getSize < maximum:
        maximum = each.getSize
        boat = each
    return boat
      
  def getShot(self,logicBoard):
    """Get position for shot with AI

    Args:
        logicBoard (list): logic board

    Returns:
        tuple: square position
    """
    if len(self.positions) != 0:
      key = ''
      found = False
      while not found:
        found = True
        for each in self.positions.keys():
          key = each
          for i in range(len(self.positions[key])):
            if self.positions[key][i] != (0,0):
              pos = self.positions[key][i]
              string = str(key)
              string = string.split(',')
              square = (int(string[0]),int(string[1]))
              self.deleteFromPosition(square,i)
              shot = (square[0]+pos[0],square[1]+pos[1])
              if shot[0] > BOARD_ROWS or shot[0] < 1 or shot[1] > BOARD_COL or shot[1] < 1:
                continue
              else:
                return shot
          found = False
          break
        if found == True:
          break
    else:
      boatSize = self.findTheLargestBoat()
      boatSize = boatSize.getSize
      randomStart = random.randint(1,10)
      for j in range(randomStart,len(logicBoard)):
        numberOfSquares = 0
        add = 0
        randomstarter = random.randint(1,4)
        for i in range(randomstarter,len(logicBoard[j])):
          if i+add >= len(logicBoard[j]):
            break
          i += add
          if logicBoard[i][j] != 2:
            numberOfSquares += 1
          else:
            add = boatSize-1
            numberOfSquares = 0
          if numberOfSquares == boatSize:
            ok = True
            for k in range(1,boatSize+1):
              if i-k >= 1:
                if logicBoard[i-k][j] == 2:
                  ok = False
                  break
            if ok:
              return (i-boatSize+1,j)
            else:
              numberOfSquares = 0
      for i in range(randomStart,len(logicBoard)):
        numberOfSquares = 0
        add = 0
        randomstarter = random.randint(1,4)
        for j in range(randomstarter,len(logicBoard[i])):
          if j+add >= len(logicBoard[i]):
            break
          j += add
          if logicBoard[i][j] != 2:
            numberOfSquares += 1
          else:
            add = boatSize-1
            numberOfSquares = 0
          if numberOfSquares == boatSize:
            ok = True
            for k in range(1,boatSize+1):
              if j-k >= 1:
                if logicBoard[i][j-k] == 2:
                  ok = False
                  break
            if ok:
              return (i,j-boatSize+1)
            else:
              numberOfSquares = 0
    return (0,0)