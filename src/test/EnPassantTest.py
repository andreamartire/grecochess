'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model import QuadBitBoard

from model.Generator import Generator
import Constants

board = QuadBitBoard.QuadBitBoard()
board.showBoard(3)

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
