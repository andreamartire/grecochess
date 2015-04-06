'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz
import Utils, Constants
from pieces import Knight, King, Bitshop, Rook, Queen, Pawn
from model import Move

class QuadBitBoard(object):
    busyCells = mpz(0)
    
    #quad bit board
    rqk = mpz(0)
    nbk = mpz(0)
    pbq = mpz(0)
    black = mpz(0)
    
    #white indexes
    whitePawnsIndexes = []
    whiteKnightIndexes = []
    whiteBitshopsIndexes = []
    whiteRooksIndexes = []
    whiteQueenIndexes = []
    whiteKingIndex = 0
    
    #black indexes
    blackPawnsIndexes = []
    blackKnightIndexes = []
    blackBitshopsIndexes = []
    blackRooksIndexes = []
    blackQueenIndexes = []
    blackKingIndex = 0
    
    def __init__(self):
        
        #white pawns
        for num in range(8,16):
            self.pbq = self.pbq.setbit(num)
            self.whitePawnsIndexes.append(Utils.getCellBitArrayById(num))
        
        #white knights
        self.nbk = self.nbk.setbit(1).setbit(6)
        self.whiteKnightIndexes = [Utils.getCellBitArrayById(1), Utils.getCellBitArrayById(6)]
        
        #white bitshops
        self.nbk = self.nbk.setbit(2).setbit(5)
        self.pbq = self.pbq.setbit(2).setbit(5)
        self.whiteBitshopsIndexes = [Utils.getCellBitArrayById(2), Utils.getCellBitArrayById(5)]
        
        #white rooks
        self.rqk = self.rqk.setbit(0).setbit(7)
        self.whiteRooksIndexes = [Utils.getCellBitArrayById(0), Utils.getCellBitArrayById(7)]
        
        #white queen
        self.rqk = self.rqk.setbit(3)
        self.pbq = self.pbq.setbit(3)
        self.whiteQueenIndexes.append(Utils.getCellBitArrayById(3))
        
        #white king
        self.nbk = self.nbk.setbit(4)
        self.rqk = self.rqk.setbit(4)
        self.whiteKingIndex = Utils.getCellBitArrayById(4)
        
        #black
        for num in range(48,64):
            self.black = self.black.setbit(num)
        
        #black pawns
        for num in range(48,56):
            self.pbq = self.pbq.setbit(num)
            self.blackPawnsIndexes.append(Utils.getCellBitArrayById(num))
        
        #black knights
        self.nbk = self.nbk.setbit(57).setbit(62)
        self.blackKnightIndexes = [Utils.getCellBitArrayById(57), Utils.getCellBitArrayById(62)]
        
        #black bitshops
        self.nbk = self.nbk.setbit(58).setbit(61)
        self.pbq = self.pbq.setbit(58).setbit(61)
        self.blackBitshopsIndexes = [Utils.getCellBitArrayById(58), Utils.getCellBitArrayById(61)]

        #black rooks
        self.rqk = self.rqk.setbit(56).setbit(63)
        self.blackRooksIndexes = [Utils.getCellBitArrayById(56), Utils.getCellBitArrayById(63)]
        
        #black queen
        self.rqk = self.rqk.setbit(59)
        self.pbq = self.pbq.setbit(59)
        self.blackQueenIndexes.append(Utils.getCellBitArrayById(59))
        
        #black king
        self.nbk = self.nbk.setbit(60)
        self.rqk = self.rqk.setbit(60)
        self.blackKingIndex = Utils.getCellBitArrayById(60)
        
    def clean(self):
        self.rqk = mpz(0)
        self.nbk = mpz(0)
        self.pbq = mpz(0)
        self.black = mpz(0)
        
        #white indexes
        self.whitePawnsIndexes = []
        self.whiteKnightIndexes = []
        self.whiteBitshopsIndexes = []
        self.whiteRooksIndexes = []
        self.whiteQueenIndexes = []
        self.whiteKingIndex = mpz(0).setbit(0)
        
        #black indexes
        self.blackPawnsIndexes = []
        self.blackKnightIndexes = []
        self.blackBitshopsIndexes = []
        self.blackRooksIndexes = []
        self.blackQueenIndexes = []
        self.blackKingIndex = mpz(0).setbit(0)
        return
    
    def setCellbyId(self, i, pieceType):
        self.rqk = self.rqk.setbit(i,0)
        self.nbk = self.nbk.setbit(i,0)
        self.pbq = self.pbq.setbit(i,0)
        self.black = self.black.setbit(i,0)
        
        if(set("rnbqkp") & set(pieceType)):
            self.black = self.black.setbit(i)
        if(pieceType == 'r'):
            self.rqk = self.rqk.setbit(i)
            self.blackRooksIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'n'):
            self.nbk = self.nbk.setbit(i)
            self.blackKnightIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'b'):
            self.pbq = self.pbq.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.blackBitshopsIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'q'):
            self.rqk = self.rqk.setbit(i)
            self.pbq = self.pbq.setbit(i)
            self.blackRooksIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'k'):
            self.rqk = self.rqk.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.blackKingIndex = Utils.getCellBitArrayById(i)
        if(pieceType == 'p'):
            self.pbq = self.pbq.setbit(i)
            self.blackPawnsIndexes += [Utils.getCellBitArrayById(i)]
        
        if(pieceType == 'R'):
            self.rqk = self.rqk.setbit(i)
            self.whiteRooksIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'N'):
            self.nbk = self.nbk.setbit(i)
            self.whiteKnightIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'B'):
            self.pbq = self.pbq.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.whiteBitshopsIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'Q'):
            self.rqk = self.rqk.setbit(i)
            self.pbq = self.pbq.setbit(i)
            self.whiteQueenIndexes += [Utils.getCellBitArrayById(i)]
        if(pieceType == 'K'):
            self.rqk = self.rqk.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.whiteKingIndex = Utils.getCellBitArrayById(i)
        if(pieceType == 'P'):
            self.pbq = self.pbq.setbit(i)
            self.whitePawnsIndexes += [Utils.getCellBitArrayById(i)]
        return
        
    def setManualConfiguration(self, stringConfig):
        #reset the board
        self.clean()
        
        for i in range(1,64):
            self.setCellbyId(i, stringConfig[i])
        return
    
    def showBoard(self, view):
        #get ordered cells indexes for gui
        cells = Utils.getCellIndexesForGui()
        
        white = (self.rqk | self.pbq | self.nbk) ^ self.black

        #extract pieces
        rooks    =  self.rqk & ~self.pbq & ~self.nbk
        knigths  = ~self.rqk & ~self.pbq &  self.nbk
        bitshops =              self.pbq &  self.nbk
        queens   =  self.rqk &  self.pbq 
        pawns    = ~self.rqk &  self.pbq & ~self.nbk
        kings    =  self.rqk             &  self.nbk
        
        #black
        blackRooks = rooks & self.black
        blackKnights = knigths & self.black
        blackBitshops = bitshops & self.black
        blackQueens = queens & self.black
        blackPawns = pawns & self.black
        blackKing = kings & self.black
        
        #white
        whiteRooks = rooks ^ self.black
        whiteKnights = knigths ^ self.black
        whiteBitshops = bitshops ^ self.black
        whiteQueens = queens ^ self.black
        whitePawns = pawns ^ self.black
        whiteKing = kings ^ self.black
        
        output = ""
        #complete
        if(view == 1):
            for i in cells:
                if(i % 8 == 0):
                    output += "\n+-----+-----+-----+-----+-----+-----+-----+-----+\n"
                    if(i < 8):
                        output = output + "|    0|    1|    2|    3|    4|    5|    6|    7|\n"
                    elif(i < 16):
                        output = output + "|    8|    9|   10|   11|   12|   13|   14|   15|\n"
                    else:
                        for j in range(i,i+8):
                            output = output + "|   "+str(j)
                        output += "|\n"
                if(self.black.getbit(i) == 1):
                    if(blackRooks.getbit(i) == 1):
                        output += "| r   "
                    elif(blackKnights.getbit(i) == 1):
                        output += "| n   "
                    elif(blackBitshops.getbit(i) == 1):
                        output += "| b   "
                    elif(blackPawns.getbit(i) == 1):
                        output += "| p   "
                    elif(blackQueens.getbit(i) == 1):
                        output += "| q   "
                    elif(blackKing.getbit(i) == 1):
                        output += "| k   "
                elif(white.getbit(i) == 1):
                    if(whiteRooks.getbit(i) == 1):
                        output += "| R   "
                    elif(whiteKnights.getbit(i) == 1):
                        output += "| N   "
                    elif(whiteBitshops.getbit(i) == 1):
                        output += "| B   "
                    elif(whitePawns.getbit(i) == 1):
                        output += "| P   "
                    elif(whiteQueens.getbit(i) == 1):
                        output += "| Q   "
                    elif(whiteKing.getbit(i) == 1):
                        output += "| K   "
                else:
                    output += "|     "
                if(i % 8 == 7): 
                    output += "|"
            output += "\n+-----+-----+-----+-----+-----+-----+-----+-----+\n"
        #only piece
        else:
            for i in cells:
                if(i % 8 == 0):
                    output += "\n"
                if(self.black.getbit(i) == 1):
                    if(blackRooks.getbit(i) == 1):
                        output += "r"
                    elif(blackKnights.getbit(i) == 1):
                        output += "n"
                    elif(blackBitshops.getbit(i) == 1):
                        output += "b"
                    elif(blackPawns.getbit(i) == 1):
                        output += "p"
                    elif(blackQueens.getbit(i) == 1):
                        output += "q"
                    elif(blackKing.getbit(i) == 1):
                        output += "k"
                elif(white.getbit(i) == 1):
                    if(whiteRooks.getbit(i) == 1):
                        output += "R"
                    elif(whiteKnights.getbit(i) == 1):
                        output += "N"
                    elif(whiteBitshops.getbit(i) == 1):
                        output += "B"
                    elif(whitePawns.getbit(i) == 1):
                        output += "P"
                    elif(whiteQueens.getbit(i) == 1):
                        output += "Q"
                    elif(whiteKing.getbit(i) == 1):
                        output += "K"
                else:
                    output += "-"
        print output
        return 
    
    def moveQuiet(self, bbFrom, bbTo):
        #get move bb
        moveBB = bbFrom | bbTo
        #if it is one among Rook, Queen, King
        if(self.rqk & bbFrom == bbFrom):
            self.rqk    = self.rqk ^ moveBB

        #if it is one among Pawn, Bitshop, Queen
        if(self.pbq & bbFrom == bbFrom):
            self.pbq    = self.pbq ^ moveBB

        #if it is one among Knight, Bitshop, King
        if(self.nbk & bbFrom == bbFrom):
            self.nbk    = self.nbk ^ moveBB

        #if it is Black
        if(self.black & bbFrom == bbFrom):
            self.black  = self.black ^ moveBB
        return