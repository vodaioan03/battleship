from utils.constants import *
import pygame
class Boat:
  
  def __init__(self,name,size,x,y,color,ui) -> None:
    self.name = name 
    self.size = size
    self.initialPosition = (x,y)
    self.position = (x,y)
    self.color = color
    self.uiInterface = ui
    self.view = None
    self.align = 'Vertical'
    self.width = SQUARE_SIZE
    self.height = self.size * SQUARE_SIZE
    self.isAdded = False
    
  def changeAlign(self):
    if not self.isAdded:
      self.width,self.height = self.height, self.width
      if self.align == 'Vertical':
        self.align = 'Horizontal'
      else:
        self.align = 'Vertical'
    
  def draw(self):
    self.view = pygame.draw.rect(self.uiInterface,self.color,[self.position[0],self.position[1],self.width,self.height])