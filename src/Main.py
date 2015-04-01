'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO precalculate bitboard and not only the dest cell
#TODO pieces' index array converted in linked list
#TODO position type from integer 32 bit to 6 bit mpz?

from structures import BitBoard, Move
from pieces import Knight, King, Pawn, Bitshop, Rook, Queen
import Utils
from gmpy import mpz

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

cells = Utils.getCellsBitArray();
for i in range(0,64):
    Utils.showBitArray(cells[i])

#bitshop's moves in a cell
movesArray = Bitshop.getMovesArray(18)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#rook's moves in a cell
movesArray = Rook.getMovesArray(38)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#queen's moves in a cell
movesArray = Queen.getMovesArray(27)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#king's moves in a cell
movesArray = King.getMovesArray(27)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#knight's moves in a cell
movesArray = Knight.getMovesArray(27)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#white pawn's moves in a cell
movesArray = Pawn.getWhiteMovesArray(10)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

#black pawn's moves in a cell
movesArray = Pawn.getBlackMovesArray(52)
currMoves = Utils.movesToBitArray(movesArray)
Utils.showBitArray(currMoves)

board = BitBoard.BitBoard()
board.showBoard()

# for i in range(1,6) + range(8,16):
#     move = Move.Move(1,1,i)
#     print move.type 
#     print bin(move.type)
# 
# v = mpz(0).setbit(3)
# z = mpz(0).setbit(0)
# print bin(v | z)