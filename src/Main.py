'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add en passant rollback

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

board.setCellbyId(52, 'p')
board.setCellbyId(54, 'p')
board.setCellbyId(37, 'P')
board.setCellbyId(35, 'P')

'''board.setCellbyId(25, 'p')
board.setCellbyId(27, 'p')
board.setCellbyId(10, 'P')
board.setCellbyId(12, 'P')'''

board.showBoard(3)

moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)

print "\nMoves:"
for move in moves:
    print move

board.executeMove(moves[1])
board.showBoard(3)

moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)

print "\nMoves:"
for move in moves:
    print move
    
board.executeMove(moves[3])
board.showBoard(3)
