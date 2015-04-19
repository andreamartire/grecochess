'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO hash positions instead of array positions

import Constants, time, Utils
from model import QuadBitBoard
from model.Engine import Engine

board = QuadBitBoard.QuadBitBoard()
'''start = time.clock()
for i in range(0,100000):
    Engine.getAllPseudoLegalMoves(board, Constants.BLACK, True)
end = time.clock()
print end - start'''

board.clean()

board.setCellbyId(4, 'K')
board.setCellbyId(0, 'R')
board.setCellbyId(7, 'R')

board.setCellbyId(27, 'n')

board.setCellbyId(60, 'k')
board.setCellbyId(56, 'r')
board.setCellbyId(63, 'r')

board.showBoard(2)

moves = Engine.getAllPseudoLegalMoves(board, Constants.BLACK, True)

for move in moves:
    print move

board.executeMove(moves[0])

board.showBoard(3)

board.rollbackLastMove()

board.showBoard(3)

