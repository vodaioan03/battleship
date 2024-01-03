from uiStuff.GUI import *
from uiStuff.uiConsole import *
import configparser
from colorama import *
  

  
class StartGame:
  
  def __init__(self,uiInterface, playerName:str) -> None:
    self.uiInterface = uiInterface
    self.playerName = playerName
    self.uiInterface.playerName(playerName)
    
  
  def playGame(self):
    self.uiInterface.startGame()

if __name__ == "__main__":
  uiOptions = {'1':UI,'2':GUI} #IF you wan't to choose you need to make another class.
  config = configparser.RawConfigParser()
  config.read('battleship\\settings.properties')
  uiInterfaceChoosen = config.get('GameInterface','gameinterface.ui')
  playerName = config.get('UserInfo','userinfo.name')
  if not uiInterfaceChoosen.isdigit or playerName == '' or uiInterfaceChoosen not in uiOptions.keys():
    print(Fore.RED + "[ERROR] Failed to start Game. Please entry 1 or 2 at the gameinterface.ui and insert Player Name." + Style.RESET_ALL)
    quit()
  uiInteface = uiOptions[uiInterfaceChoosen]()
  startGame = StartGame(uiInteface,playerName)
  startGame.playGame() # Start Game