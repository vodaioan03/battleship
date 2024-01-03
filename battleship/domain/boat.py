from utils.constants import *
from domain.board import *
import pygame
class Boat:
  
  def __init__(self,name,img,size,x,y,color,ui,Board) -> None:
    self.name = name
    self.size = size
    self.initialPosition = (x,y)
    self.position = (x,y)
    self.color = color
    self.uiInterface = ui
    self.view = None
    self.align = 'Vertical'
    self.width = SQUARE_SIZE
    self.height = self.size * self.width
    self.isAdded = False
    self.boardSquare = (-1,-1)
    self.board = Board
    self.shots = 0
    if self.uiInterface != 'Console':
      self.setImg(pygame.transform.scale(img,(self.width,self.width*size)))
      
  def setImg(self,img):
    self.img = img
    
  def setView(self,view):
    self.view = view
    
  def reInit(self):
    self.position = self.initialPosition
    self.view = None
    self.isAdded = False
    self.boardSquare = (-1,-1)
    self.shots = 0
    
    
  def setAlign(self,align):
    self.width,self.height = self.height, self.width
    self.align = align
    
  def setBoardSquare(self,i,z):
    self.boardSquare = (i,z)
    
  def draw(self):
    x = y = None
    if self.boardSquare[0] != -1:
      boatRect = self.board.boardDomain.getFromBoard(self.boardSquare[0],self.boardSquare[1])
      x=boatRect.x
      y=boatRect.y
    if x != None:
      self.setView(pygame.draw.rect(self.uiInterface,self.color,[x,y,self.width,self.height],1))
      self.uiInterface.blit(self.img,(x,y))
    else:
      self.setView(pygame.draw.rect(self.uiInterface,self.color,[self.position[0],self.position[1],self.width,self.height],1))
      self.uiInterface.blit(self.img,(self.position[0],self.position[1]))
    
  def setSquareSize(self,size):
    if self.width == SQUARE_SIZE or self.width == SQUARE_SIZE_MINI:
      self.width = size
      self.height = self.width * self.size
      if self.uiInterface != 'Console':
        self.setImg(pygame.transform.scale(self.img,(self.width,self.width*self.size)))
    else:
      self.height = size
      self.width = self.height * self.size
      if self.uiInterface != 'Console':
        self.setImg(pygame.transform.rotate(self.img, -90))
        self.setImg(pygame.transform.scale(self.img,(self.height,self.height*self.size)))
        self.setImg(pygame.transform.rotate(self.img, 90))
      
  def __str__(self) -> str:
    return f"{self.name} | {self.position} | {self.boardSquare} | {self.view}"
      
  def __repr__(self) -> str:
    return self.__str__()