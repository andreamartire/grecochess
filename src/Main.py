'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO hash positions instead of array positions

import Constants, time, Utils
from model import QuadBitBoard
from model.Generator import Generator

board = QuadBitBoard.QuadBitBoard()
'''start = time.clock()
for i in range(0,100000):
    moves = Engine.getAllPseudoLegalMoves(board, Constants.WHITE, True)

    board.executeMove(moves[2])
    
    board.rollbackLastMove()
end = time.clock()
print end - start'''

board.clean()

board.setCellbyId(55, 'P')

board.showBoard(3)

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)

print "\nMoves:"
for move in moves:
    print move
    
board.executeMove(moves[3])

board.showBoard(3)

board.rollbackLastMove()

board.showBoard(3)
