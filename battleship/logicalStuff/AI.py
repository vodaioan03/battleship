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
    self.positions = {} # {'':N- i-1,S- i+1,V- j-1,E- j+1}
    print("AI")
    
  def deleteSunk(self,boat):
    for i in range(len(self.boats)):
      if self.boats[i] == boat:
        self.boats.remove(boat)
        break
      
  def showBoats(self):
    print(self.boats)
    
  def addPosition(self,square):
    self.positions[f'{square[0]},{square[1]}'] = [(-1,0),(1,0),(0,-1),(0,1)]
    print(self.positions)
    
  def deleteFromPosition(self,square,index):
    self.positions[f'{square[0]},{square[1]}'][index] = (0,0)
    self.deletePosition(square)
    
    
  def deletePosition(self,square):
    delete = True
    for each in self.positions[f'{square[0]},{square[1]}']:
      if each != (0,0):
        delete = False
    if delete == True:
      print("delete")
      del self.positions[f'{square[0]},{square[1]}']
      
  def getShot(self):
    if len(self.positions) != 0:
      key = ''
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
              print(f"SHOT FAIL: {shot}")
              continue
            else:
              return shot
    return (0,0)