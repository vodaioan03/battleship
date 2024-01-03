from logicalStuff.boardLogic import *
from domain.boat import *
from utils.constants import *

import random
import time

class UI:
  
  def __init__(self) -> None:
    self.uiInterface = 'Console'
    self.isPlaying = False
    self.commands = {}
    
  def playerName(self,playerName):
    self.playerName = playerName
    
    
  #####################3FROM GUI ###################################
    
  def addBoards(self):
    self.playerBoard = BoardLogic(self.uiInterface)
    self.computerBoard = BoardLogic(self.uiInterface)
  
  def spawnRandomBoats(self, boardUse:Board,boats:list):
    boardUse.boardReinit()
    for each in boats:
      if each.getAlign == 'Horizontal':
        self.changeAlign(each)
        each.setAlign('Vertical')
    self.boardview(boardUse)
    for boat in boats:
      added = False
      while not added:
        number = random.randint(1,100)
        if number % 2 == 0:
          self.changeAlign(boat)
          if boat.getAlign == 'Horizontal':
            boat.setAlign('Vertical')
          else:
            boat.setAlign('Horizontal')
        added = boardUse.spawnBoat(boat)
  
    
  ################################################################################
  
  ## FUNCTIONS
  
  def showBoard(self,command):
    print("Show Board\n")
    board = self.playerBoard.getLogicBoard
    for i in board:
      if i != []:
        string = ''
        for j in range(1,len(i)):
          if isinstance(i[j],Boat):
            string += f'| {i[j].getName[0]} '
          else:
            string += f'| {i[j]} '
        print(string)
    pass
  
  def addBoat(self,command):
    print("Add boat")
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 4:
      raise ValueError('Incorrect Command')
    else:
      if command[1] not in self.boats.keys():
        raise ValueError('Invalid boat!')
      if not command[2].isdigit() or not command[3].isdigit():
        raise ValueError('Invalid X or Y')
      if int(command[2]) > 10 or int(command[3]) > 10 or int(command[2]) < 1 or int(command[3]) < 1:
        raise ValueError('X and Y bigger than 10.')
      boat = self.playerBoard.getBoat(command[1])
      square = (int(command[2]),int(command[3]))
      if self.playerBoard.checkValability(boat,boat.align,square[0],square[1]) and boat.getBoardSquare == (-1,-1):
        boat.boardSquare = square
        self.playerBoard.verifyCoordsinSquare(boat)
      else:
        raise ValueError('Boat already added or position is already ocuppied.')
  
  def deleteBoat(self,command):
    print("delete boat")
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 2:
      raise ValueError('Incorrect Command')
    else:
      if command[1] not in self.boats.keys():
        raise ValueError('Invalid boat!')
      boat = self.playerBoard.getBoat(command[1])
      if boat.getBoardSquare != (-1,-1):
        self.playerBoard.boatTaken(boat)
      else:
        raise ValueError("Boat isn't added to Board!")
  
  def rotateBoat(self,command):
    print("Rottate boat")
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 2:
      raise ValueError('Incorrect Command')
    else:
      if command[1] not in self.boats.keys():
        raise ValueError('Invalid boat!')
      boat = self.playerBoard.getBoat(command[1])
      if boat.getBoardSquare != (-1,-1):
        raise ValueError("You can't rotate a boat already added. Delete and rotate.")
      boat.rotateAlign()
      print('Boat has been rotated!')
  
  def shuffle(self,command):
    print("Shuffle")
    pass
  
  def shotBoat(self,command):
    print("Shot boat")
    pass
  
  def showStats(self,command):
    print("show Satts")
    pass
    
  def exiting(self,command):
    """Exiting function
    """
    print("Exiting game. Bye bye!")
    self.isPlaying = False
    quit()
  
  #PRINT FUNCTIONS
  
  def showCommands(self,command):
    print("\n- - - - - - - Commands - - - - - - - \n")
    print("commands | Show list with all commands")
    print("show | Showing your board [WITH BOATS]")
    print("add <boat> <x> <y> | Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2")
    print("delete <boat> | Delete a boat from board.")
    print("rotate <boat> [ONLY IF BOAT ISN'T ADDED]| Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2")
    print("shuffle | Generate random positions for boats")
    print("start [ONLY WHEN ALL BOATS ARE ON TABLE] | Generate random boats for computer and start the game!")
    print("shot <x> <y> | Add shot on computer Board.")
    print("stats | Number of shots are on boats")
    print("exit | Exiting game.")
    print("- - - - - - - - - - - - - - - - - - - -\n")
    
  def printLogicBoard(self,boardUse:Board):
    board = boardUse.getLogicBoard
    for i in board:
      if i != []:
        string = ''
        for j in board[i]:
          string += f'| {board[i][j]} '
        print(string)
    
  def inputCommand(self):
    commandInput = input("Type the command: ").strip()
    commandInput = commandInput.split(' ')
    if commandInput[0] in self.commands.keys():
      try:
        self.commands[commandInput[0]](commandInput)
      except ValueError as e:
        print(e)
        
  def startGame(self):
    self.isPlaying = True
    self.commands = {'commands':self.showCommands,'show':self.showBoard,'add':self.addBoat,'delete':self.deleteBoat,'rotate':self.rotateBoat,'shuffle':self.shuffle,'start':self.startGame,'shot':self.shotBoat,'stats':self.showStats,'exit':self.exiting}
    self.boats = {'carrier':0,'battleship':1,'destroyer':2,'submarine':3,'patrol':4}
    self.showCommands('')
    self.addBoards()
    self.playerBoard.createBoats()
    self.computerBoard.createBoats()
    while self.isPlaying:
      self.inputCommand()