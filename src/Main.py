'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

import Constants, time, Utils
from model import QuadBitBoard
from engine import MinMax

from model.Generator import Generator
from model.MoveCache import MoveCache
from engine.AlphaBeta import AlphaBeta

board = QuadBitBoard.QuadBitBoard()
board.showBoard(3)

moves = AlphaBeta.calculateSolution(board, Constants.WHITE, 6)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

'''board.executeMove(moves[3])
board.showBoard(3)

moves = AlphaBeta.calculateSolution(board, Constants.BLACK, 6)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[2])
board.showBoard(3)

moves = AlphaBeta.calculateSolution(board, Constants.WHITE, 6)
for i in range(0,len(moves)):
    print str(i) + "=" + str(moves[i])

board.executeMove(moves[0])
board.showBoard(4)
MoveCache.cleanUnusefulMoves(board)'''