'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO hash positions instead of array positions

import Constants, time, Utils
from model import QuadBitBoard, Engine
from model.Move import Move, CAPTURE, QUIET

board = QuadBitBoard.QuadBitBoard()
'''start = time.clock()
for i in range(0,100000):
    Engine.getAllPseudoLegalMoves(board, Constants.BLACK)
end = time.clock()
print end - start'''

board.clean()

board.setCellbyId(4, 'K')
board.setCellbyId(7, 'R')
board.setCellbyId(0, 'R')

board.setCellbyId(60, 'k')
board.setCellbyId(56, 'r')
board.setCellbyId(63, 'r')

board.setCellbyId(40, 'N')

board.showBoard(2)

moves = Engine.getAllPseudoLegalMoves(board, Constants.BLACK, True)

