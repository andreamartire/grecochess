'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz
import Utils, Constants, Move
from pieces import Knight

class BitBoard(object):
    busyCells = mpz(0)
    
    #white bitboard
    whitePieces = mpz(0)
    whitePawns = mpz(0)
    whiteKnight = mpz(0)
    whiteBitshops = mpz(0)
    whiteRooks = mpz(0)
    whiteQueen = mpz(0)
    whiteKing = mpz(0)
    
    #white indexes
    whitePawnsIndexes = []
    whiteKnightIndexes = []
    whiteBitshopsIndexes = []
    whiteRooksIndexes = []
    whiteQueenIndexes = []
    whiteKingIndex = 0
    
    #black bitboard
    blackPieces = mpz(0)
    blackPawns = mpz(0)
    blackKnight = mpz(0)
    blackBitshops = mpz(0)
    blackRooks = mpz(0)
    blackQueen = mpz(0)
    blackKing = mpz(0)
    
    #black indexes
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
        
    def clean(self):
        self.whitePieces = mpz(0)
        self.whitePawns = mpz(0)
        self.whiteKnight = mpz(0)
        self.whiteBitshops = mpz(0)
        self.whiteRooks = mpz(0)
        self.whiteQueen = mpz(0)
        self.whiteKing = mpz(0)
        
        #white indexes
        self.whitePawnsIndexes = []
        self.whiteKnightIndexes = []
        self.whiteBitshopsIndexes = []
        self.whiteRooksIndexes = []
        self.whiteQueenIndexes = []
        self.whiteKingIndex = 0
        
        #black bitboard
        self.blackPieces = mpz(0)
        self.blackPawns = mpz(0)
        self.blackKnight = mpz(0)
        self.blackBitshops = mpz(0)
        self.blackRooks = mpz(0)
        self.blackQueen = mpz(0)
        self.blackKing = mpz(0)
        
        #black indexes
        self.blackPawnsIndexes = []
        self.blackKnightIndexes = []
        self.blackBitshopsIndexes = []
        self.blackRooksIndexes = []
        self.blackQueenIndexes = []
        self.blackKingIndex = 0
        return
    
    def setCellbyId(self, i, pieceType):
        if(set("rnbqkp") & set(pieceType)):
            self.blackPieces = self.blackPieces.setbit(i)
        if(pieceType == 'r'):
            self.blackRooks = self.blackRooks.setbit(i)
            self.blackRooksIndexes += [i]
        if(pieceType == 'n'):
            self.blackKnight = self.blackKnight.setbit(i)
            self.blackKnightIndexes += [i]
        if(pieceType == 'b'):
            self.blackBitshops = self.blackBitshops.setbit(i)
            self.blackBitshopsIndexes += [i]
        if(pieceType == 'q'):
            self.blackQueen = self.blackQueen.setbit(i)
            self.blackRooksIndexes += [i]
        if(pieceType == 'k'):
            self.blackKing = self.blackKing.setbit(i)
            self.blackKingIndex = i
        if(pieceType == 'p'):
            self.blackPawns = self.blackPawns.setbit(i)
            self.blackPawnsIndexes += [i]
        
        if(set('RNBQKP') & set(pieceType)):
            self.whitePieces = self.whitePieces.setbit(i)
        if(pieceType == 'R'):
            self.whiteRooks = self.whiteRooks.setbit(i)
            self.whiteRooksIndexes += [i]
        if(pieceType == 'N'):
            self.whiteKnight = self.whiteKnight.setbit(i)
            self.whiteKnightIndexes += [i]
        if(pieceType == 'B'):
            self.whiteBitshops = self.whiteBitshops.setbit(i)
            self.whiteBitshopsIndexes += [i]
        if(pieceType == 'Q'):
            self.whiteQueen = self.whiteQueen.setbit(i)
            self.whiteQueenIndexes += [i]
        if(pieceType == 'K'):
            self.whiteKing = self.whiteKing.setbit(i)
            self.whiteKingIndex = i
        if(pieceType == 'P'):
            self.whitePawns = self.whitePawns.setbit(i)
            self.whitePawnsIndexes += [i]
        return
        
    def setManualConfiguration(self, stringConfig):
        #reset the board
        self.clean()
        
        for i in range(1,64):
            self.setCellbyId(i, stringConfig[i])
        return
    
    def showBoard(self, type):
        #get ordered cells indexes for gui
        cells = Utils.getCellIndexesForGui()
        
        output = ""
        #complete
        if(type == 1):
            for i in cells:
                if(i % 8 == 0):
                    output += "\n ---- ---- ---- ---- ---- ---- ---- ---- \n"
                    if(i < 8):
                        output = output + "|   0|   1|   2|   3|   4|   5|   6|   7|\n"
                    elif(i < 16):
                        output = output + "|   8|   9|  10|  11|  12|  13|  14|  15|\n"
                    else:
                        for j in range(i,i+8):
                            output = output + "|  "+str(j)
                        output += "|\n"
                if(self.blackPieces.getbit(i) == 1):
                    if(self.blackRooks.getbit(i) == 1):
                        output += "|r   "
                    elif(self.blackKnight.getbit(i) == 1):
                        output += "|n   "
                    elif(self.blackBitshops.getbit(i) == 1):
                        output += "|b   "
                    elif(self.blackPawns.getbit(i) == 1):
                        output += "|p   "
                    elif(self.blackQueen.getbit(i) == 1):
                        output += "|q   "
                    elif(self.blackKing.getbit(i) == 1):
                        output += "|k   "
                elif(self.whitePieces.getbit(i) == 1):
                    if(self.whiteRooks.getbit(i) == 1):
                        output += "|R   "
                    elif(self.whiteKnight.getbit(i) == 1):
                        output += "|N   "
                    elif(self.whiteBitshops.getbit(i) == 1):
                        output += "|B   "
                    elif(self.whitePawns.getbit(i) == 1):
                        output += "|P   "
                    elif(self.whiteQueen.getbit(i) == 1):
                        output += "|Q   "
                    elif(self.whiteKing.getbit(i) == 1):
                        output += "|K   "
                else:
                    output += "|    "
                if(i % 8 == 7): 
                    output += "|"
            output += "\n ---- ---- ---- ---- ---- ---- ---- ---- \n"
        #only piece
        elif(type == 0):
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
    
    def getAllPseudoLegalMoves(self, color):
        
        #detect busy cells
        self.busyCells = self.whitePieces | self.blackPieces
        
        knightMoves = self.getKnightMoves(color)
        
        print knightMoves
        
        return
    
    def getKnightMoves(self, color):
        movesList = []
        if(color == Constants.WHITE):
            #White Knights
            for startPos in self.whiteKnightIndexes:
                #get all moves
                allMoves = Knight.getMovesArray(startPos)
                #for each move
                for destPos in allMoves:
                    #get bit array for dest cell
                    destCell = Utils.getCellBitArrayById(destPos)
                    #if dest cell is busy
                    if((self.busyCells & destCell) == destCell):
                        #if black piece occupies dest cell
                        if((self.blackPieces & destCell) == destCell):
                            #black piece. add capture move
                            #print "Capture Move: " + str(startPos) + "-" + str(destPos)
                            movesList.append(Move.Move(startPos, destPos, Move.CAPTURE))
                    else:
                        #add quiet move
                        #print "Quiet Move: " + str(startPos) + "-" + str(destPos)
                        movesList.append(Move.Move(startPos, destPos, Move.QUIET))
        elif(color == Constants.BLACK):
            #Black Knights
            for startPos in self.blackKnightIndexes:
                #get all moves
                allMoves = Knight.getMovesArray(startPos)
                #for each move
                for destPos in allMoves:
                    #get bit array for dest cell
                    destCell = Utils.getCellBitArrayById(destPos)
                    #if dest cell is busy
                    if((self.busyCells & destCell) == destCell):
                        #if white piece occupies dest cell
                        if((self.whitePieces & destCell) == destCell):
                            #white piece. add capture move
                            #print "Capture Move: " + str(startPos) + "-" + str(destPos)
                            movesList.append(Move.Move(startPos, destPos, Move.CAPTURE))
                    else:
                        #add quiet move
                        #print "Quiet Move: " + str(startPos) + "-" + str(destPos)
                        movesList.append(Move.Move(startPos, destPos, Move.QUIET))
        
        for move in movesList:
            print move