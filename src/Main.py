'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO precalculate bitboard and not only the dest cell
#TODO position type from integer 32 bit to 6 bit mpz?

from structures import BitBoard
import Constants
from pieces import Bitshop
import time

board = BitBoard.BitBoard()
start = time.clock()
for i in range(0,100000):
    board.getAllPseudoLegalMoves(Constants.BLACK)
end = time.clock()
print end - start

board = BitBoard.BitBoard()
board.getAllPseudoLegalMoves(Constants.BLACK)
