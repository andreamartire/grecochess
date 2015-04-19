'''
Created on 14/apr/2015

@author: Andrea Martire
'''
from gmpy import mpz

#white
#king side
spacesWhiteKingCastle = mpz(0).setbit(5).setbit(6)
safeCellsWhiteKingCastle = mpz(0).setbit(4).setbit(5).setbit(6)
shadowRqkWhiteKingCastle = mpz(0).setbit(4).setbit(5).setbit(6).setbit(7)
shadowNbkWhiteKingCastle = mpz(0).setbit(4).setbit(6)
#queen side
spacesWhiteQueenCastle = mpz(0).setbit(3).setbit(2).setbit(1)
safeCellsWhiteQueenCastle = mpz(0).setbit(4).setbit(3).setbit(2)
shadowRqkWhiteQueenCastle = mpz(0).setbit(4).setbit(3).setbit(2).setbit(0)
shadowNbkWhiteQueenCastle = mpz(0).setbit(4).setbit(2)

#black
#king side
spacesBlackKingCastle = mpz(0).setbit(61).setbit(62)
safeCellsBlackKingCastle = mpz(0).setbit(60).setbit(61).setbit(62)
shadowRqkBlackKingCastle = mpz(0).setbit(60).setbit(61).setbit(62).setbit(63)
shadowNbkBlackKingCastle = mpz(0).setbit(60).setbit(62)
#queen side
spacesBlackQueenCastle = mpz(0).setbit(59).setbit(58).setbit(57)
safeCellsBlackQueenCastle = mpz(0).setbit(60).setbit(59).setbit(58)
shadowRqkBlackQueenCastle = mpz(0).setbit(60).setbit(59).setbit(58).setbit(56)
shadowNbkBlackQueenCastle = mpz(0).setbit(60).setbit(58)



    
