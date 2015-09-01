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

'''print "Ordered"
moves = Generator.quicksort(moves)
for move in moves:
    print move'''
    
'''move = AlphaBeta.calculateSolution(board, Constants.WHITE, 8)
print "MinMaxSolution"
print move'''

board.clean()

board.setCellbyId(4, 'K')
board.setCellbyId(0, 'R')
board.setCellbyId(31, 'r')
board.setCellbyId(7, 'R')

board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, 0, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[7])
board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, 0, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[25])
board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, 0, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
    
board.executeMove(moves[12])
board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, 0, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
    
board.executeMove(moves[19])
board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, 0, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
