'''
Created on 14/apr/2015

@author: Andrea Martire
'''
from gmpy import mpz

#white

#king side
_spacesWhiteKingCastle = mpz(0).setbit(5).setbit(6)
_safeCellsWhiteKingCastle = mpz(0).setbit(5).setbit(6)
#queen side
_spacesWhiteQueenCastle = mpz(0).setbit(3).setbit(2).setbit(1)
_safeCellsWhiteQueenCastle = mpz(0).setbit(3).setbit(2)

#black

#king side
_spacesBlackKingCastle = mpz(0).setbit(61).setbit(62)
_safeCellsBlackKingCastle = mpz(0).setbit(61).setbit(62)
#queen side
_spacesBlackQueenCastle = mpz(0).setbit(59).setbit(58).setbit(57)
_safeCellsBlackQueenCastle = mpz(0).setbit(59).setbit(58)

def spacesWhiteKingCastle():
    return _spacesWhiteKingCastle;

def safeCellsWhiteKingCastle():
    return _safeCellsWhiteKingCastle;

def spacesWhiteQueenCastle():
    return _spacesWhiteQueenCastle;

def safeCellsWhiteQueenCastle():
    return _safeCellsWhiteQueenCastle;

def spacesBlackKingCastle():
    return _spacesBlackKingCastle;

def safeCellsBlackKingCastle():
    return _safeCellsBlackKingCastle;

def spacesBlackQueenCastle():
    return _spacesBlackQueenCastle;

def safeCellsBlackQueenCastle():
    return _safeCellsBlackQueenCastle;

