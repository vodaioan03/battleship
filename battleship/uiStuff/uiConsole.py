from logicalStuff.boardLogic import *
from domain.boat import *
from logicalStuff.AI import *
from utils.constants import *
from uiStuff.errors import *
from texttable import Texttable

import random
import time
from colorama import *

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
      raise InvalidCommand()
    if command[1] != 'player' and command[1] != 'computer':
      raise InvalidPlayer()
    boardUse = self.playerBoard
    if command[1] == 'computer':
      boardUse = self.computerBoard
    board = boardUse.getBoardDomain
    if command[1] == 'player':
      print(board)
    else:
      print(board.printOnlyShots())
  
  def addBoat(self,command,*args):
    if self.afterStrategy:
      raise GameStaredError()
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 4:
      raise InvalidCommand()
    else:
      if command[1] not in self.boats.keys():
        raise ErrorException('Invalid boat!')
      if not command[2].isdigit() or not command[3].isdigit():
        raise ParamsNumbersError()
      if int(command[2]) > 10 or int(command[3]) > 10 or int(command[2]) < 1 or int(command[3]) < 1:
        raise ErrorException('X and Y bigger than 10 or smaller than 1.')
      boat = self.playerBoard.getBoat(command[1])
      square = (int(command[2]),int(command[3]))
      if self.playerBoard.checkValability(boat,boat.align,square[0],square[1]) and boat.getBoardSquare == (-1,-1):
        boat.boardSquare = square
        self.playerBoard.verifyCoordsinSquare(boat)
      else:
        raise ErrorException('Boat already added or position is already ocuppied.')
  
  def deleteBoat(self,command,*args):
    if self.afterStrategy:
      raise GameStaredError()
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 2:
      raise InvalidCommand()
    else:
      if command[1] not in self.boats.keys():
        raise ErrorException('Invalid boat!')
      boat = self.playerBoard.getBoat(command[1])
      if boat.getBoardSquare != (-1,-1):
        self.playerBoard.boatTaken(boat)
      else:
        raise ErrorException("Boat isn't added to Board!")
  
  def rotateBoat(self,command,*args):
    if self.afterStrategy:
      raise GameStaredError()
    for i in range(len(command)):
      command[i].strip()
      command[i].lower()
    if len(command) != 2:
      raise InvalidCommand()
    else:
      if command[1] not in self.boats.keys():
        raise ErrorException('Invalid boat!')
      boat = self.playerBoard.getBoat(command[1])
      if boat.getBoardSquare != (-1,-1):
        raise ErrorException("You can't rotate a boat already added. Delete and rotate.")
      boat.rotateAlign()
      self.succesPrint('Boat has been rotated!')
      
  
  def shuffle(self,command,*args):
    if self.afterStrategy:
      raise GameStaredError()
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
      raise GameStaredError()
    if self.playerBoard.readyStart:
      print(Fore.GREEN + "\n\n - - - - -  Game Starts! Good Luck! - - - - -\n\n" + Style.RESET_ALL)
      self.shuffle('',self.computerBoard)
      self.afterStrategy = True
    else:
      raise ErrorException("You can start after all boats are added on the board.")
  
  def shotBoat(self,command,*args):
    if not self.afterStrategy:
      raise GameNotStarted()
    if len(command) != 3:
      raise InvalidCommand()
    if not command[1].isdigit() or not command[2].isdigit():
      raise ErrorException("X and Y needs to be numbers.")
    if int(command[1]) > 10 or int(command[2]) > 10 or int(command[1]) < 1 or int(command[2]) < 1:
        raise ErrorException('X and Y bigger than 10 or smaller than 1.')
    boardUse = args[0]
    if boardUse == self.computerBoard and self.turn != 'Player':
      raise ErrorException('Not your turn!')
    square = (int(command[1]),int(command[2]))
    if boardUse.checkShoot(square):
      boat = boardUse.getBoatForCoords(square[0],square[1])
      message = boardUse.boardShot(square)
      print(Fore.LIGHTRED_EX + f"{args[1]}: {message}" + Style.RESET_ALL)
      if isinstance(boat, Boat):
        if boardUse != self.computerAI.board:
          self.computerAI.addPosition(square)
        if boat.getSunk:
          print(Fore.MAGENTA +f"{boat.name} sunk!"+ Style.RESET_ALL)
          if boardUse != self.computerAI.board:
            self.computerAI.deleteSunk(boat)
      self.changeTurn()
      if self.turn == 'Computer':
        self.start_time = time.time()
        print(Fore.CYAN +"\n Computer turn! Waiting..." + Style.RESET_ALL)
    else:
      raise ErrorException("Invalid Shot! Shot again!")
  
  def showStats(self,command,*args):
    boardUse = args[0]
    if len(command) != 2:
      raise InvalidCommand()
    text = command[1].strip()
    text = command[1].lower()
    if text != 'player' and text != 'computer':
      raise InvalidPlayer()
    if text == 'player':
      boardUse = self.computerBoard
    stats = boardUse.getStats()
    print(Fore.MAGENTA + f"\n= = = = Stats {text} = = = =\n"+ Style.RESET_ALL)
    print(Fore.CYAN + f"Total Shots: {stats[0]}"+ Style.RESET_ALL)
    print(Fore.CYAN + f"Boats Shots: {stats[1]}"+ Style.RESET_ALL)
    print(Fore.CYAN + f"Water Shots: {stats[2]}"+ Style.RESET_ALL)
    print(Fore.CYAN + f"Remaining Boats: {stats[3]}\n"+ Style.RESET_ALL)
    print(Fore.MAGENTA + ' = = = = = = = = = = = = = =' + Style.RESET_ALL)
    
  def exiting(self,command,*args):
    """Exiting function
    """
    self.succesPrint("Exiting game. Bye bye!")
    self.isPlaying = False
    quit()
  
  #PRINT FUNCTIONS
  
  def showCommands(self,command,*args):
    print(Fore.MAGENTA +"\n- - - - - - - Commands - - - - - - - \n"+ Style.RESET_ALL)
    print(Fore.YELLOW + "commands | Show list with all commands"+ Style.RESET_ALL)
    print(Fore.YELLOW + "show <player> | Showing your board [WITH BOATS]"+ Style.RESET_ALL)
    print(Fore.YELLOW + "add <boat> <x> <y> | Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2"+ Style.RESET_ALL)
    print(Fore.YELLOW + "delete <boat> | Delete a boat from board."+ Style.RESET_ALL)
    print(Fore.YELLOW + "rotate <boat> [ONLY IF BOAT ISN'T ADDED]| Boats: Carrier - 5, Battleship - 4, Destroyer - 3, Submarine - 3, Patrol - 2"+ Style.RESET_ALL)
    print(Fore.YELLOW + "shuffle | Generate random positions for boats"+ Style.RESET_ALL)
    print(Fore.YELLOW + "start [ONLY WHEN ALL BOATS ARE ON TABLE] | Generate random boats for computer and start the game!"+ Style.RESET_ALL)
    print(Fore.YELLOW + "shot <x> <y> | Add shot on computer Board."+ Style.RESET_ALL)
    print(Fore.YELLOW + "stats <player> | Statistics for player/computer"+ Style.RESET_ALL)
    print(Fore.YELLOW + "exit | Exiting game."+ Style.RESET_ALL)
    print(Fore.MAGENTA + "- - - - - - - - - - - - - - - - - - - -\n"+ Style.RESET_ALL)
    
  def succesPrint(self,msg):
    print(Fore.GREEN + 'SUCCES: ' + str(msg) + Style.RESET_ALL)
  
    
    
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
      except ErrorException as e:
        print(Fore.RED + 'ERROR: ' + str(e) + Style.RESET_ALL)
    else:
      raise InvalidCommand()
        
  def checkWinner(self):
    if self.playerBoard.verifyWinner:
      print(Fore.RED + "\n\n\n\n You Loose! Computer Wins!\n\n\n\n" + Style.RESET_ALL)
      self.isPlaying = False
      quit()
    elif self.computerBoard.verifyWinner:
      print(Fore.GREEN + "\n\n\n\n You Won! Computer Loose!\n\n\n\n" + Style.RESET_ALL)
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
          commandShot = commandShot.split(' ')
          self.shotBoat(commandShot,self.playerBoard,'Player')
      else:
        try:
          self.inputCommand()
        except ErrorException as e:
          print(Fore.RED + 'ERROR: ' + str(e) + Style.RESET_ALL)