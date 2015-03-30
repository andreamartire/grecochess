'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

from pieces import Rook, Bitshop

#calculate pieces' moves only once
_diagonalMoves = Bitshop.bitshopMoves()
_orthogonalMoves = Rook.rookMoves()

def diagonalMoves():
    return _diagonalMoves

def orthogonalMoves():
    return _orthogonalMoves

def queenMoves():
    return [_diagonalMoves] + [_diagonalMoves];