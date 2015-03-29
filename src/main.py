'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz
import BitBoard, Moves

board = BitBoard.BitBoard()
board.showBoard()

knightMoves = Moves.knightMoves()
print knightMoves

kingMoves = Moves.kingMoves()
print kingMoves

blackPawnMoves = Moves.blackPawnMoves()
print blackPawnMoves

whitePawnMoves = Moves.whitePawnMoves()
print whitePawnMoves

bitshopMoves = Moves.bitshopMoves()
print bitshopMoves

rookMoves = Moves.rookMoves()
print rookMoves

