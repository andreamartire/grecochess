'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

import Constants, time, Utils
from model import QuadBitBoard
from engine import MinMax, AlphaBeta

from model.Generator import Generator

board = QuadBitBoard.QuadBitBoard()
board.clean()

board.setCellbyId(4, "K")
board.setCellbyId(7, "R")
board.setCellbyId(0, "R")

board.showBoard(3)

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
