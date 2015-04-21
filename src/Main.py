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

board.setCellbyId(4, 'K')
board.setCellbyId(0, 'R')
board.setCellbyId(7, 'R')
board.setCellbyId(8, 'P')
board.setCellbyId(9, 'P')
board.setCellbyId(10, 'P')
board.setCellbyId(11, 'P')
board.setCellbyId(12, 'P')
board.setCellbyId(13, 'P')
board.setCellbyId(14, 'P')
board.setCellbyId(15, 'P')

board.setCellbyId(60, 'k')
board.setCellbyId(56, 'r')
board.setCellbyId(63, 'r')
board.setCellbyId(48, 'p')
board.setCellbyId(49, 'p')
board.setCellbyId(50, 'p')
board.setCellbyId(51, 'p')
board.setCellbyId(52, 'p')
board.setCellbyId(53, 'p')
board.setCellbyId(54, 'p')
board.setCellbyId(55, 'p')

board.showBoard(2)

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)

print "\nMoves:"
for move in moves:
    print move

board.executeMove(moves[2])
board.showBoard(3)

board.rollbackLastMove()

board.showBoard(3)

