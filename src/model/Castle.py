'''
Created on 14/apr/2015

@author: Andrea Martire
'''
from gmpy import mpz

#white
_spacesWhiteKingCastle = mpz(0).setbit(5).setbit(6)
_spacesWhiteQueenCastle = mpz(0).setbit(3).setbit(2).setbit(1)

#black
_spacesBlackKingCastle = mpz(0).setbit(61).setbit(62)
_spacesBlackQueenCastle = mpz(0).setbit(59).setbit(58).setbit(57)

def spacesWhiteKingCastle():
    return _spacesWhiteKingCastle;

def spacesWhiteQueenCastle():
    return _spacesWhiteQueenCastle;

def spacesBlackKingCastle():
    return _spacesBlackKingCastle;

def spacesBlackQueenCastle():
    return _spacesBlackQueenCastle;

