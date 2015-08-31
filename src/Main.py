'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add en passant rollback

import Constants, time, Utils
from model import QuadBitBoard
from Engine import MinMax, AlphaBeta

board = QuadBitBoard.QuadBitBoard()

move = AlphaBeta.calculateSolution(board, Constants.WHITE, 4)

print "MinMaxSolution"
print move

board.showBoard(3)



