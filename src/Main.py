'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO precalculate bitboard and not only the dest cell
#TODO pieces' index array converted in linked list
#TODO position type from integer 32 bit to 6 bit mpz?

#TODO Impedire di collocare pedoni in settima e in prima riga per evitare problemi nel calcolo delle mosse

from structures import BitBoard
import Constants
from pieces import Bitshop

board = BitBoard.BitBoard()
#board.clean()

board.setCellbyId(20, 'q')
board.setCellbyId(16, 'p')

board.showBoard(1)

Bitshop.getMovesArray(6)
board.getAllPseudoLegalMoves(Constants.WHITE)
