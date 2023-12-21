from utils.constants import *
import pygame
class Board:
  
  def __init__(self) -> None:
    print("Init board")
    self.board = [[0 for _ in range(BOARD_COL)] for _ in range(BOARD_ROWS)]
    for i in range(BOARD_ROWS):
      print(self.board[i])