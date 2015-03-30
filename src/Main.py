'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz

import BitBoard
from pieces import Knight, King, Pawn, Bitshop, Rook, Queen

board = BitBoard.BitBoard()
board.showBoard()

knightMoves = Knight.knightMoves()
print "Knight: " + str(knightMoves)

kingMoves = King.kingMoves()
print "King: " + str(kingMoves)

blackPawnMoves = Pawn.blackPawnMoves()
print "Black Pawn: " + str(blackPawnMoves)

whitePawnMoves = Pawn.whitePawnMoves()
print "White Pawn: " + str(whitePawnMoves)

bitshopMoves = Bitshop.bitshopMoves()
print "Bitshop: " + str(bitshopMoves)

rookMoves = Rook.rookMoves()
print "Rook: " + str(rookMoves)

queenMoves = Queen.queenMoves()
print "Queen: " + str(queenMoves)
