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
board.showBoard(3)

'''print "Ordered"
moves = Generator.quicksort(moves)
for move in moves:
    print move'''
    
'''move = AlphaBeta.calculateSolution(board, Constants.WHITE, 8)
print "MinMaxSolution"
print move'''

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[7])
board.showBoard(3)
    
moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[15])
board.showBoard(3)
    
moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
    
board.executeMove(moves[10])
board.showBoard(3)

hashcode = board.getHash()

moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])
    
board.executeMove(moves[1])
board.showBoard(3)

boardBackup = QuadBitBoard.QuadBitBoard()
boardBackup.setHash(hashcode)
boardBackup.showBoard(3)
