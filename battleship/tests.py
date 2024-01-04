from domain.board import *
from domain.boat import *
from logicalStuff.AI import *
from logicalStuff.boardLogic import *

import unittest


class TestBoardFunctions(unittest.TestCase):

    def setUp(self):
      self.computerBoard = BoardLogic('Console')
      self.playerBoard = BoardLogic('Console')
      
    def test_clearBoard(self):
      self.computerBoard.boardReinit()
      self.playerBoard.boardReinit()
      stats = self.computerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
      stats = self.playerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
    
    def test_emptyBoard(self):
      self.computerBoard.boardDomain.emptyBoard
      self.assertEqual(self.computerBoard.boardDomain.getBoard, [[]])
      self.playerBoard.boardDomain.emptyBoard
      self.assertEqual(self.playerBoard.boardDomain.getBoard, [[]])
    
    def test_addToBoard(self):
      self.computerBoard.boardDomain.addToBoard('manel',0)
      self.assertEqual(self.computerBoard.boardDomain.getBoard[0],['manel'])
      self.playerBoard.boardDomain.addToBoard('manel')
      self.assertEqual(self.playerBoard.boardDomain.getBoard[1],'manel')
    
    def test_getFromLogicalBoard(self):
      self.assertEqual(self.computerBoard.boardDomain.getFromLogicalBoard(1,1),0)
      self.assertEqual(self.playerBoard.boardDomain.getFromLogicalBoard(1,1),0)
      pass

    def test_getFromBoard(self):
      self.playerBoard.boardDomain.addToBoard([[]],0)
      self.computerBoard.boardDomain.addToBoard([[]],0)
      self.assertEqual(self.computerBoard.boardDomain.getFromBoard(0,0),[[]])
      self.assertEqual(self.playerBoard.boardDomain.getFromBoard(0,0),[[]])
    
    def test_getSquaresize(self):
      self.assertEqual(self.computerBoard.boardDomain.getSquareSize,self.computerBoard.boardDomain.squareSize)
      self.assertEqual(self.playerBoard.boardDomain.getSquareSize,self.playerBoard.boardDomain.squareSize)
    
    def test_getBoats(self):
      self.assertEqual(self.computerBoard.boardDomain.getBoats,self.computerBoard.boardDomain.boats)
      self.assertEqual(self.playerBoard.boardDomain.getBoats,self.playerBoard.boardDomain.boats)
    
    def test_getBoard(self):
      self.assertEqual(self.computerBoard.boardDomain.getBoard,self.computerBoard.boardDomain.board)
      self.assertEqual(self.playerBoard.boardDomain.getBoard,self.playerBoard.boardDomain.board)
    def test_getTotalShots(self):
      self.assertEqual(self.computerBoard.boardDomain.getTotalShots,self.computerBoard.boardDomain.totalShots)
      self.assertEqual(self.playerBoard.boardDomain.getTotalShots,self.playerBoard.boardDomain.totalShots)
      
    def test_setBoats(self):
      self.computerBoard.boardDomain.setBoats(['boat1'])
      self.playerBoard.boardDomain.setBoats(['boat2'])
      self.assertEqual(self.computerBoard.boardDomain.getBoats,['boat1'])
      self.assertEqual(self.playerBoard.boardDomain.getBoats,['boat2'])
      
    def test_setSquareSize(self):
      self.computerBoard.boardDomain.setSquareSize(25)
      self.assertEqual(self.computerBoard.boardDomain.getSquareSize,25)
      self.assertEqual(self.playerBoard.boardDomain.getSquareSize,SQUARE_SIZE)
  
    def test_getOneNeeded(self):
      self.assertEqual(self.computerBoard.boardDomain.getOneNeeded,self.computerBoard.boardDomain.oneNeeded)
      self.assertEqual(self.playerBoard.boardDomain.getOneNeeded,self.playerBoard.boardDomain.oneNeeded)
    def test_getLogicBoard(self):
      self.assertEqual(self.computerBoard.boardDomain.getLogicBoard,self.computerBoard.boardDomain.logicBoard)
      self.assertEqual(self.playerBoard.boardDomain.getLogicBoard,self.playerBoard.boardDomain.logicBoard)
    def test_getOnes(self):
      self.assertEqual(self.computerBoard.boardDomain.getOnes,self.computerBoard.boardDomain.ones)
      self.assertEqual(self.playerBoard.boardDomain.getOnes,self.playerBoard.boardDomain.ones)
    
    def test_getBoatShots(self):
      self.assertEqual(self.computerBoard.boardDomain.getBoatShots,self.computerBoard.boardDomain.boatShots)
      self.assertEqual(self.playerBoard.boardDomain.getBoatShots,self.playerBoard.boardDomain.boatShots)
    
    def test_setValueToLogicalBoard(self):
      self.playerBoard.boardDomain.setValueToLogicalBoard(1,1,2)
      self.computerBoard.boardDomain.setValueToLogicalBoard(1,1,2)
      self.assertEqual(self.computerBoard.boardDomain.getFromLogicalBoard(1,1),2)
      self.assertEqual(self.playerBoard.boardDomain.getFromLogicalBoard(1,1),2)
    
    def test_addOnes(self):
      oneComp = self.computerBoard.boardDomain.getOnes
      onePL = self.playerBoard.boardDomain.getOnes
      self.computerBoard.boardDomain.addOnes
      self.playerBoard.boardDomain.addOnes
      self.assertEqual(self.computerBoard.boardDomain.getOnes,oneComp+1)
      self.assertEqual(self.playerBoard.boardDomain.getOnes,onePL+1)
      
    def test_deleteOnes(self):
      oneComp = self.computerBoard.boardDomain.getOnes
      onePL = self.playerBoard.boardDomain.getOnes
      self.computerBoard.boardDomain.addOnes
      self.playerBoard.boardDomain.addOnes
      self.playerBoard.boardDomain.deleteOnes
      self.computerBoard.boardDomain.deleteOnes
      self.assertEqual(self.computerBoard.boardDomain.getOnes,oneComp)
      self.assertEqual(self.playerBoard.boardDomain.getOnes,onePL)
    def test_addTotalShots(self):
      oneComp = self.computerBoard.boardDomain.getTotalShots
      onePL = self.playerBoard.boardDomain.getTotalShots
      self.computerBoard.boardDomain.addTotalShots()
      self.playerBoard.boardDomain.addTotalShots()
      self.assertEqual(self.computerBoard.boardDomain.getTotalShots,oneComp+1)
      self.assertEqual(self.playerBoard.boardDomain.getTotalShots,onePL+1)
    def test_addBoatShots(self):
      oneComp = self.computerBoard.boardDomain.getBoatShots
      onePL = self.playerBoard.boardDomain.getBoatShots
      self.computerBoard.boardDomain.addBoatShots()
      self.playerBoard.boardDomain.addBoatShots()
      self.assertEqual(self.computerBoard.boardDomain.getBoatShots,oneComp+1)
      self.assertEqual(self.playerBoard.boardDomain.getBoatShots,onePL+1)
        
class TestBoatFunctions(unittest.TestCase):
    
    def setUp(self):
      self.boat = Boat('Carrier',BOAT_CARRIER,10,105,COLOR_BLACK,'Console',self,IMG_BOAT_CARRIER)
      
    def test_setImg(self):
      self.boat.setImg('img')
      self.assertEqual(self.boat.getImg,'img')
    
    def test_setView(self):
      self.boat.setView('img')
      self.assertEqual(self.boat.view,'img')
    
    def test_reInit(self):
      self.boat.setView('img')
      self.boat.reInit()
      self.assertEqual(self.boat.view,None)
      
    def test_setAlign(self):
      self.boat.setAlign('Horizontal')
      self.assertEqual(self.boat.getAlign,'Horizontal')
      self.boat.setAlign('Vertical')
      self.assertEqual(self.boat.getAlign,'Vertical')
    
    def test_getBoardSquare(self):
      self.assertEqual(self.boat.getBoardSquare,self.boat.boardSquare)
    
    def test_getImg(self):
      self.assertEqual(self.boat.getImg,self.boat.img)
    
    def test_getWidth(self):
      self.assertEqual(self.boat.getWidth,self.boat.width)
    
    def test_getHeight(self):
      self.assertEqual(self.boat.getHeight,self.boat.height)
    
    def test_getColor(self):
      self.assertEqual(self.boat.getColor,self.boat.color)
    
    def test_getPosition(self):
      self.assertEqual(self.boat.getPosition,self.boat.position)
    
    def test_getAlign(self):
      self.assertEqual(self.boat.getAlign,self.boat.align)
    
    def test_getName(self):
      self.assertEqual(self.boat.name,'Carrier')
    def test_getSize(self):
      self.assertEqual(self.boat.getSize,self.boat.size)
    def test_getSunk(self):
      self.assertEqual(self.boat.getSunk,False)
    def test_setBoardSquare(self):
      self.boat.setBoardSquare(1,1)
      self.assertEqual(self.boat.boardSquare,(1,1))
    def test_rotateAlign(self):
      self.boat.rotateAlign()
      self.assertEqual(self.boat.align,'Horizontal')
    def test_setBoatSquareSize(self):
      self.boat.setBoatSquareSize(12)
      self.assertEqual(self.boat.width,12)
    
      
class TestAI(unittest.TestCase):
    
    def setUp(self):
      self.computerBoard = BoardLogic('Console')
      self.playerBoard = BoardLogic('Console')
      self.computerBoard.createBoats()
      self.computerAI = AI(self.computerBoard)
      
    def test_deleteSunk(self):
      boat = self.computerBoard.getBoats
      boat = boat[0]
      self.computerAI.deleteSunk(boat)
      self.assertEqual(len(self.computerAI.boats), 4)
      
    def test_addPosition(self):
      self.computerAI.addPosition((1,1))
      self.assertEqual(len(self.computerAI.positions),1)
    def test_deleteFromPosition(self):
      self.computerAI.addPosition((1,1))
      self.computerAI.deleteFromPosition((1,1),0)
      self.assertEqual(self.computerAI.positions['1,1'][0],(0,0))
    def test_deletePosition(self):
      self.computerAI.addPosition((1,1))
      self.computerAI.deleteFromPosition((1,1),0)
      self.computerAI.deleteFromPosition((1,1),1)
      self.computerAI.deleteFromPosition((1,1),2)
      self.computerAI.deleteFromPosition((1,1),3)
      self.assertEqual(len(self.computerAI.positions),0)
    def test_findTheLargestBoat(self):
      self.assertEqual(self.computerAI.findTheLargestBoat(),self.computerBoard.boardDomain.boats[4])
      self.computerAI.deleteSunk(self.computerBoard.boardDomain.boats[4])
      self.assertEqual(self.computerAI.findTheLargestBoat(),self.computerBoard.boardDomain.boats[2])
    def test_getShot(self):
      shot = (0,0)
      shot = self.computerAI.getShot(self.computerBoard.getLogicBoard)
      self.assertNotEqual(shot,(0,0))
      
class TestBoardLogic(unittest.TestCase):
    
    def setUp(self):
      self.computerBoard = BoardLogic('Console')
      self.playerBoard = BoardLogic('Console')
      self.computerBoard.createBoats()
      self.playerBoard.createBoats()
    
    def test_checkValability(self):
      self.assertEqual(self.playerBoard.checkValability(self.playerBoard.getBoats[0],'Vertical',1,1),True)
      self.assertEqual(self.playerBoard.checkValability(self.playerBoard.getBoats[0],'Vertical',9,9),False)
      self.assertEqual(self.computerBoard.checkValability(self.computerBoard.getBoats[0],'Vertical',1,1),True)
      self.assertEqual(self.computerBoard.checkValability(self.computerBoard.getBoats[1],'Horizontal',9,9),False)
    
    def test_addToBoard(self):
      self.computerBoard.addToBoard('Entity')
      self.assertEqual(self.computerBoard.boardDomain.getBoard[1],'Entity')
      self.computerBoard.addToBoard('Entity2')
      self.assertEqual(self.computerBoard.boardDomain.getBoard[2],'Entity2')
      
    def test_emptyBoard(self):
      self.computerBoard.addToBoard('Entity2')
      self.computerBoard.emptyBoard
      self.assertEqual(len(self.computerBoard.boardDomain.board),1)
      
      self.playerBoard.addToBoard('Entity2')
      self.playerBoard.emptyBoard
      self.assertEqual(len(self.playerBoard.boardDomain.board),1)
      
    def test_getBoats(self):
      boats = self.computerBoard.getBoats
      self.assertEqual(boats,self.computerBoard.boardDomain.boats)
      boats = self.playerBoard.getBoats
      self.assertEqual(boats,self.playerBoard.boardDomain.boats)
    
    def test_setBoats(self):
      self.computerBoard.setBoats(['Boat1','Boat2'])
      self.assertEqual(self.computerBoard.getBoats,['Boat1','Boat2'])
      self.playerBoard.setBoats(['Boat1','Boat2'])
      self.assertEqual(self.playerBoard.getBoats,['Boat1','Boat2'])
    
    def test_createBoats(self):
      self.computerBoard.createBoats()
      self.assertEqual(len(self.computerBoard.getBoats),5)
      self.playerBoard.createBoats()
      self.assertEqual(len(self.playerBoard.getBoats),5)
    
    
    def test_getBoat(self):
      self.assertEqual(self.computerBoard.getBoat('Maniel'),None)
      self.assertEqual(self.playerBoard.getBoat('Barcaaalicu'),None)
      self.assertEqual(self.computerBoard.getBoat('Marcelcu'),None)
      self.assertEqual(self.playerBoard.getBoat('Tettuielele'),None)
      self.assertEqual(self.computerBoard.getBoat('TestBoat'),None)
      self.assertEqual(self.playerBoard.getBoat('Testubotut'),None)
    
    def test_readyStart(self):
      self.assertEqual(self.computerBoard.readyStart,False)
      self.assertEqual(self.playerBoard.readyStart,False)
      self.assertEqual(self.playerBoard.readyStart,False)
      
    def test_getLogicBoard(self):
      self.assertEqual(self.computerBoard.getLogicBoard,self.computerBoard.boardDomain.logicBoard)
      self.assertEqual(self.playerBoard.getLogicBoard,self.playerBoard.boardDomain.logicBoard)
    
    def test_setSquareSize(self):
      self.computerBoard.setSquareSize(21)
      self.assertEqual(self.computerBoard.boardDomain.squareSize,21)
      self.computerBoard.setSquareSize(1)
      self.assertEqual(self.computerBoard.boardDomain.squareSize,1)
      self.playerBoard.setSquareSize(21)
      self.assertEqual(self.playerBoard.boardDomain.squareSize,21)
      self.playerBoard.setSquareSize(1)
      self.assertEqual(self.playerBoard.boardDomain.squareSize,1)
    
    def test_verifyWinner(self):
      self.assertEqual(self.computerBoard.verifyWinner,False)
      self.assertEqual(self.playerBoard.verifyWinner,False)
      self.computerBoard.setWinner()
      self.playerBoard.setWinner()
      self.assertEqual(self.computerBoard.verifyWinner,True)
      self.assertEqual(self.playerBoard.verifyWinner,True)
    
    def test_setWinner(self):
      self.computerBoard.setWinner()
      self.assertEqual(self.computerBoard.boardDomain.getOneNeeded,self.computerBoard.boardDomain.getBoatShots)
      self.assertNotEqual(self.playerBoard.boardDomain.getOneNeeded,self.playerBoard.boardDomain.getOnes)
      self.playerBoard.setWinner()
      self.assertEqual(self.playerBoard.boardDomain.getOneNeeded,self.playerBoard.boardDomain.getBoatShots)
    
    def test_verifyPositionBoat(self):
      self.assertEqual(self.computerBoard.verifyPositionBoat((1,1)),None)
      self.assertEqual(self.computerBoard.verifyPositionBoat((2,1)),None)
      self.assertEqual(self.computerBoard.verifyPositionBoat((3,1)),None)
      self.assertEqual(self.computerBoard.verifyPositionBoat((4,1)),None)
      self.assertEqual(self.computerBoard.verifyPositionBoat((5,1)),None)
      self.assertEqual(self.computerBoard.verifyPositionBoat((6,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((1,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((2,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((3,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((4,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((5,1)),None)
      self.assertEqual(self.playerBoard.verifyPositionBoat((6,1)),None)
    
    def test_boardReinit(self):
      self.computerBoard.boardReinit()
      self.playerBoard.boardReinit()
      stats = self.computerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
      stats = self.playerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
    
    def test_spawnBoat(self):
      self.computerBoard.spawnBoat(self.computerBoard.getBoats[1])
      self.assertNotEqual(self.computerBoard.getBoats[1],(-1,-1))
    
    def test_sendShot(self):
      shot = (-1,-1)
      shot = self.playerBoard.sendShot()
      self.assertNotEqual(shot,(-1,-1))
      shot = self.playerBoard.sendShot()
      shot = self.playerBoard.sendShot()
      shot = self.playerBoard.sendShot()
      self.assertNotEqual(shot,(-1,-1))
      shot = (-1,-1)
      shot = self.computerBoard.sendShot()
      self.assertNotEqual(shot,(-1,-1))
      shot = self.computerBoard.sendShot()
      shot = self.computerBoard.sendShot()
      shot = self.computerBoard.sendShot()
      self.assertNotEqual(shot,(-1,-1))
    
    def test_getStats(self):
      self.computerBoard.boardReinit()
      self.playerBoard.boardReinit()
      stats = self.computerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
      stats = self.playerBoard.getStats()
      self.assertEqual(stats[0],0)
      self.assertEqual(stats[1],0)
      self.assertEqual(stats[2],0)
      self.assertEqual(stats[3],17)
    