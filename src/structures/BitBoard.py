'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz
import Utils

class BitBoard(object):
    #white bitboard
    whitePieces = 0
    whitePawns = 0
    whiteKnight = 0
    whiteBitshops = 0
    whiteRooks = 0
    whiteQueen = 0
    whiteKing = 0
    
    #white indexes
    whitePiecesIndexes = []
    whitePawnsIndexes = []
    whiteKnightIndexes = []
    whiteBitshopsIndexes = []
    whiteRooksIndexes = []
    whiteQueenIndexes = []
    whiteKingIndex = 0
    
    #black bitboard
    blackPieces = 0
    blackPawns = 0
    blackKnight = 0
    blackBitshops = 0
    blackRooks = 0
    blackQueen = 0
    blackKing = 0
    
    #black indexes
    blackPiecesIndexes = []
    blackPawnsIndexes = []
    blackKnightIndexes = []
    blackBitshopsIndexes = []
    blackRooksIndexes = []
    blackQueenIndexes = []
    blackKingIndex = 0
    
    def __init__(self):                
        #White Pieces
        self.whitePieces = mpz(0)
        for num in range(0,16):
            self.whitePieces = self.whitePieces.setbit(num)
            self.whitePiecesIndexes.append(num)
        #print 'White Pieces=' + bin(self.whitePieces)
        
        self.whitePawns = mpz(0)
        for num in range(8,16):
            self.whitePawns = self.whitePawns.setbit(num)
            self.whitePawnsIndexes.append(num)
        #print 'White Pawns=' + bin(self.whitePawns)
        
        self.whiteKnight = mpz(0).setbit(1).setbit(6)
        self.whiteKnightIndexes = [1, 6]
        #print 'White Horses=' + bin(self.whiteKnight)
        
        self.whiteBitshops = mpz(0).setbit(2).setbit(5)
        self.whiteBitshopsIndexes = [2, 5]
        #print 'White Bitshops=' + bin(self.whiteBitshops)
        
        self.whiteRooks = mpz(0).setbit(0).setbit(7)
        self.whiteRooksIndexes = [0, 7]
        #print 'White Rooks=' + bin(self.whiteRooks)
        
        self.whiteQueen = mpz(0).setbit(3)
        self.whiteQueenIndexes.append(3)
        #print 'White Queen=' + bin(self.whiteQueen)
        
        self.whiteKing = mpz(0).setbit(4)
        self.whiteKingIndex = 4
        #print 'White King=' + bin(self.whiteKing)
        
        #Black Pieces
        self.blackPieces = mpz(0)
        for num in range(48,64):
            self.blackPieces = self.blackPieces.setbit(num)
            self.blackPiecesIndexes.append(num)
        #print 'Black Pieces\t' + bin(blackPieces)
        
        self.blackPawns = mpz(0)
        for num in range(48,56):
            self.blackPawns = self.blackPawns.setbit(num)
            self.blackPawnsIndexes.append(num)
        #print 'Black Pawns=' + bin(self.blackPawns)
        
        self.blackKnight = mpz(0).setbit(57).setbit(62)
        self.blackKnightIndexes = [57, 62]
        #print 'Black Horses\t' + bin(self.blackKnight)
        
        self.blackBitshops = mpz(0).setbit(58).setbit(61)
        self.blackBitshopsIndexes = [58, 61]
        #print 'Black Bitshops\t' + bin(self.blackBitshops)
        
        self.blackRooks = mpz(0).setbit(56).setbit(63)
        self.blackRooksIndexes = [56, 63]
        #print 'Black Rooks\t' + bin(self.blackRooks)
        
        self.blackQueen = mpz(0).setbit(59)
        self.blackQueenIndexes.append(59)
        #print 'Black Queen\t' + bin(self.blackQueen)
        
        self.blackKing = mpz(0).setbit(60)
        self.blackKingIndex = 60
        #print 'Black King\t' + bin(self.blackKing)

    def showBoard(self):
        #get ordered cells indexes for gui
        cells = Utils.getCellIndexesForGui()
        
        output = ""
        for i in cells:
            if(i % 8 == 0):
                output += "\n"
            if(self.blackPieces.getbit(i) == 1):
                if(self.blackRooks.getbit(i) == 1):
                    output += "r"
                elif(self.blackKnight.getbit(i) == 1):
                    output += "n"
                elif(self.blackBitshops.getbit(i) == 1):
                    output += "b"
                elif(self.blackPawns.getbit(i) == 1):
                    output += "p"
                elif(self.blackQueen.getbit(i) == 1):
                    output += "q"
                elif(self.blackKing.getbit(i) == 1):
                    output += "k"
            elif(self.whitePieces.getbit(i) == 1):
                if(self.whiteRooks.getbit(i) == 1):
                    output += "R"
                elif(self.whiteKnight.getbit(i) == 1):
                    output += "N"
                elif(self.whiteBitshops.getbit(i) == 1):
                    output += "B"
                elif(self.whitePawns.getbit(i) == 1):
                    output += "P"
                elif(self.whiteQueen.getbit(i) == 1):
                    output += "Q"
                elif(self.whiteKing.getbit(i) == 1):
                    output += "K"
            else:
                output += "-" 
        print output
        return 
    
    def getAllLegalMoves(self):
        #for each piece
            #get pseudo legal moves
            #remove illegal moves
            #add to move list
        return