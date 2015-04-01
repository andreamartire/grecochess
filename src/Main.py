'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO precalculate bitboard and not only the dest cell
#TODO pieces' index array converted in linked list
#TODO position type from integer 32 bit to 6 bit mpz?

from structures import BitBoard
import Constants


board = BitBoard.BitBoard()
#board.clean()

board.setCellbyId(21, 'n')
board.setCellbyId(15, 'K')
board.setCellbyId(31, 'k')
board.setCellbyId(6, 'q')
board.setCellbyId(4, 'b')

board.getAllPseudoLegalMoves(Constants.BLACK)

board.showBoard(0)
