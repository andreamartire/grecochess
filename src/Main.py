'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add en passant rollback

import Constants, time, Utils
from model import QuadBitBoard
from Engine import MinMax, AlphaBeta

from model.Generator import Generator

board = QuadBitBoard.QuadBitBoard()

'''moves = Generator.getAllPseudoLegalMoves(board, 1, True)
for move in moves:
    print move

print "Ordered"
moves = Generator.quicksort(moves)
for move in moves:
    print move'''
    
move = AlphaBeta.calculateSolution(board, Constants.WHITE, 8)
print "MinMaxSolution"
print move

board.showBoard(2)



