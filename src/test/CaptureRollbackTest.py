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

board.setCellbyId(5, "B")
board.setCellbyId(33, "p")

board.showBoard(3)

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
