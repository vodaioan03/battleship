from logicalStuff.boardLogic import *
from domain.boat import *
from logicalStuff.AI import *
from utils.constants import *

import random
import time

class UI:
  
  def __init__(self) -> None:
    self.uiInterface = 'Console'
    self.isPlaying = False
    self.afterStrategy = False
    self.commands = {}
    self.boats = {}
    self.turn = 'Player'
    self.startTimer = 0
    
  def playerName(self,playerName):
    self.playerName = playerName
    
  def changeTurn(self):
    if self.turn == 'Player':
      self.turn = 'Computer'
    else:
      self.turn = 'Player'
    
  #####################3FROM GUI ###################################
    
  def addBoards(self):
    self.playerBoard = BoardLogic()
    self.computerBoard = BoardLogic()
  
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
  
  def showBoard(self,command,*args):
    print("\n")
    if len(command) != 2:
      raise ValueError('Invalid Command or Parameters.')
    if command[1] != 'player' and command[1] != 'computer':
      raise ValueError('Invalid Player! Type <player> or <computer>.')
    boardUse = self.playerBoard
    if command[1] == 'computer':
      boardUse = self.computerBoard
    board = boardUse.getLogicBoard
    for i in board:
      if i != []:
        string = ''
        for j in range(1,len(i)):
          if isinstance(i[j],Boat):
            string += f'| {i[j].getName[0]} '
          elif i[j] == 2:
            string += f"| X "
          else:
            string += f'| {i[j]} '
        print(string)
  
  def addBoat(self,command,*args):
    if self.afterStrategy:
      raise ValueError("Can't use this command after game started!")
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
        raise ValueError('X and Y bigger than 10 or smaller than 1.')
      boat = self.playerBoard.getBoat(command[1])
      square = (int(command[2]),int(command[3]))
      if self.playerBoard.checkValability(boat,boat.align,square[0],square[1]) and boat.getBoardSquare == (-1,-1):
        boat.boardSquare = square
        self.playerBoard.verifyCoordsinSquare(boat)
      else:
        raise ValueError('Boat already added or position is already ocuppied.')
  
  def deleteBoat(self,command,*args):
    if self.afterStrategy:
      raise ValueError("Can't use this command after game started!")
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
  
  def rotateBoat(self,command,*args):
    if self.afterStrategy:
      raise ValueError("Can't use this command after game started!")
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
  
  def shuffle(self,command,*args):
    if self.afterStrategy:
      raise ValueError("Can't use this command after game started!")
    boardUse = args[0]
    boardUse.boardReinit()
    for each in boardUse.getBoats:
      if each.getAlign == 'Horizontal':
        each.rotateAlign()
    for boat in boardUse.getBoats:
      added = False
      while not added:
        number = random.randint(1,100)
        if number % 2 == 0:
          boat.rotateAlign()
        added = boardUse.spawnBoat(boat)
        
  def startPlaying(self,command,*args):
    if self.afterStrategy:
      raise ValueError("Can't use this command after game started!")
    if self.playerBoard.readyStart:
      print("\n\n - - - - -  Game Starts! Good Luck! - - - - -\n\n")
      self.shuffle('',self.computerBoard)
      self.afterStrategy = True
    else:
      raise ValueError("You can start after all boats are added on the board.")
  
  def shotBoat(self,command,*args):
    if not self.afterStrategy:
      raise ValueError("Can't use this command before game started!")
    if len(command) != 3:
      raise ValueError('Incorrect Command')
    if not command[1].isdigit() or not command[2].isdigit():
      raise ValueError("X and Y needs to be numbers.")
    if int(command[1]) > 10 or int(command[2]) > 10 or int(command[1]) < 1 or int(command[2]) < 1:
        raise ValueError('X and Y bigger than 10 or smaller than 1.')
    boardUse = args[0]
    if boardUse == self.computerBoard and self.turn != 'Player':
      raise ValueError('Not your turn!')
    square = (int(command[1]),int(command[2]))
    if boardUse.checkShoot(square):
      boat = boardUse.getBoat(square[0],square[1])
      message = boardUse.boardShot(square)
      print(f"{args[1]}: {message}")
      if isinstance(boat, Boat):
        if boardUse != self.computerAI.board:
          self.computerAI.addPosition(square)
        if boat.getSunk:
          print(f"{boat.name} sunk!")
          if boardUse != self.computerAI.board:
            self.computerAI.deleteSunk(boat)
      self.changeTurn()
      if self.turn == 'Computer':
        self.start_time = time.time()
        print("\n Computer turn! Waiting...")
    else:
      raise ValueError("Invalid Shot! Shot again!")
  
  def showStats(self,command,*args):
    boardUse = args[0]
    if len(command) != 2:
      raise ValueError('Incorrect Command or Params!')
    text = command[1].strip()
    text = command[1].lower()
    if text != 'player' and text != 'computer':
      raise ValueError('Invalid Player! Type <player> or <computer>.')
    if text == 'player':
      boardUse = self.computerBoard
    stats = boardUse.getStats()
    print(f"\n= = = = Stats {text} = = = =")
    print(f"Total Shots: {stats[0]}")
    print(f"Boats Shots: {stats[1]}")
    print(f"Water Shots: {stats[2]}")
    print(f"Remaining Boats: {stats[3]}\n")
    
  def exiting(self,command,*args):
    """Exiting function
    """
    print("Exiting game. Bye bye!")
    self.isPlaying = False
    quit()
  
  #PRINT FUNCTIONS
  
  def showCommands(self,command,*args):
    print("\n- - - - - - - Commands - - - - - - - \n")
    print("commands | Show list with all commands")
    print("show <player> | Showing your board [WITH BOATS]")
    print("add <boat> <x> <y> | Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2")
    print("delete <boat> | Delete a boat from board.")
    print("rotate <boat> [ONLY IF BOAT ISN'T ADDED]| Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2")
    print("shuffle | Generate random positions for boats")
    print("start [ONLY WHEN ALL BOATS ARE ON TABLE] | Generate random boats for computer and start the game!")
    print("shot <x> <y> | Add shot on computer Board.")
    print("stats <player> | Statistics for player/computer")
    print("exit | Exiting game.")
    print("- - - - - - - - - - - - - - - - - - - -\n")
    
    
  def inputCommand(self):
    commandInput = input("Type the command: ").strip()
    commandInput = commandInput.split(' ')
    if commandInput[0] == 'winc':
      self.playerBoard.setWinner()
    elif commandInput[0] == 'winp':
      self.computerBoard.setWinner()
    if commandInput[0] in self.commands.keys():
      try:
        if commandInput[0] == 'shot':
          self.commands[commandInput[0]](commandInput,self.computerBoard,'Computer')
        else:
          self.commands[commandInput[0]](commandInput,self.playerBoard)
      except ValueError as e:
        print(e)
    else:
      raise ValueError('Invalid command! Type again!')
        
  def checkWinner(self):
    if self.playerBoard.verifyWinner:
      print("\n\n\n\n You Loose! Computer Wins!\n\n\n\n")
      self.isPlaying = False
      quit()
    elif self.computerBoard.verifyWinner:
      print("\n\n\n\n You Win! Computer Loose!\n\n\n\n")
      self.isPlaying = False
      quit()
        
  def startGame(self):
    self.isPlaying = True
    self.commands = {'commands':self.showCommands,'show':self.showBoard,'add':self.addBoat,'delete':self.deleteBoat,'rotate':self.rotateBoat,'shuffle':self.shuffle,'start':self.startPlaying,'shot':self.shotBoat,'stats':self.showStats,'exit':self.exiting}
    self.boats = {'carrier':0,'battleship':1,'destroyer':2,'submarine':3,'patrol':4}
    self.showCommands('')
    self.addBoards()
    self.playerBoard.createBoats()
    self.computerBoard.createBoats()
    
    self.computerAI = AI(self.computerBoard)
  
    while self.isPlaying:
      self.checkWinner()
      if self.turn == 'Computer':
        self.endtime = time.time()
        if self.endtime - self.start_time > 2:
          shot = False
          square = (0,0)
          while square == (0,0) or not self.playerBoard.checkShoot(square):
            square = self.computerAI.getShot(self.playerBoard.getLogicBoard)
            if square == (0,0):
              break
          if square != (0,0):
            shot = True
          while not shot:
            square = (random.randint(1,10),random.randint(1,10))
            if self.playerBoard.checkShoot(square):
              shot = True
          commandShot = f'shot {square[0]} {square[1]}'
          print(f"COMMAND COMPUTER: {commandShot}")
          commandShot = commandShot.split(' ')
          self.shotBoat(commandShot,self.playerBoard,'Player')
      else:
        try:
          self.inputCommand()
        except ValueError as e:
          print(e)