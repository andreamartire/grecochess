'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from gmpy import mpz
import Utils, Constants
from model import Move, Castle, EnPassant

EMPTY_BIT_BOARD = mpz(0)

class QuadBitBoard(object):
    busyCells = mpz(0)
    
    moveHistory = []
    moveSize = 0
    
    #quad bit board
    rqk = mpz(0)
    nbk = mpz(0)
    pbq = mpz(0)
    black = mpz(0)
    
    #white indexes
    whitePawnsIndexes = {}
    whiteKnightIndexes = {}
    whiteBitshopsIndexes = {}
    whiteRooksIndexes = {}
    whiteQueenIndexes = {}
    whiteKingIndex = {}
    
    #black indexes
    blackPawnsIndexes = {}
    blackKnightIndexes = {}
    blackBitshopsIndexes = {}
    blackRooksIndexes = {}
    blackQueenIndexes = {}
    blackKingIndex = {}
    
    whiteCastleExecuted = 0;
    blackCastleExecuted = 0;
    
    def __init__(self):
        
        #white pawns
        for num in range(8,16):
            self.pbq = self.pbq.setbit(num)
            self.whitePawnsIndexes[Utils.getCellBitArrayById(num)] = 1
        
        #white knights
        self.nbk = self.nbk.setbit(1).setbit(6)
        self.whiteKnightIndexes[Utils.getCellBitArrayById(1)] = 1
        self.whiteKnightIndexes[Utils.getCellBitArrayById(6)] = 1
        
        #white bitshops
        self.nbk = self.nbk.setbit(2).setbit(5)
        self.pbq = self.pbq.setbit(2).setbit(5)
        self.whiteBitshopsIndexes[Utils.getCellBitArrayById(2)] = 1
        self.whiteBitshopsIndexes[Utils.getCellBitArrayById(5)] = 1
        
        #white rooks
        self.rqk = self.rqk.setbit(0).setbit(7)
        self.whiteRooksIndexes[Utils.getCellBitArrayById(0)] = 1
        self.whiteRooksIndexes[Utils.getCellBitArrayById(7)] = 1
        
        #white queen
        self.rqk = self.rqk.setbit(3)
        self.pbq = self.pbq.setbit(3)
        self.whiteQueenIndexes[Utils.getCellBitArrayById(3)] = 1
        
        #white king
        self.nbk = self.nbk.setbit(4)
        self.rqk = self.rqk.setbit(4)
        self.whiteKingIndex[Utils.getCellBitArrayById(4)] = 1
        
        #black
        for num in range(48,64):
            self.black = self.black.setbit(num)
        
        #black pawns
        for num in range(48,56):
            self.pbq = self.pbq.setbit(num)
            self.blackPawnsIndexes[Utils.getCellBitArrayById(num)] = 1
        
        #black knights
        self.nbk = self.nbk.setbit(57).setbit(62)
        self.blackKnightIndexes[Utils.getCellBitArrayById(57)] = 1
        self.blackKnightIndexes[Utils.getCellBitArrayById(62)] = 1
        
        #black bitshops
        self.nbk = self.nbk.setbit(58).setbit(61)
        self.pbq = self.pbq.setbit(58).setbit(61)
        self.blackBitshopsIndexes[Utils.getCellBitArrayById(58)] = 1
        self.blackBitshopsIndexes[Utils.getCellBitArrayById(61)] = 1

        #black rooks
        self.rqk = self.rqk.setbit(56).setbit(63)
        self.blackRooksIndexes[Utils.getCellBitArrayById(56)] = 1
        self.blackRooksIndexes[Utils.getCellBitArrayById(63)] = 1
        
        #black queen
        self.rqk = self.rqk.setbit(59)
        self.pbq = self.pbq.setbit(59)
        self.blackQueenIndexes[Utils.getCellBitArrayById(59)] = 1
        
        #black king
        self.nbk = self.nbk.setbit(60)
        self.rqk = self.rqk.setbit(60)
        self.blackKingIndex[Utils.getCellBitArrayById(60)] = 1
        
    def clean(self):
        self.rqk = mpz(0)
        self.nbk = mpz(0)
        self.pbq = mpz(0)
        self.black = mpz(0)
        
        #white indexes
        self.whitePawnsIndexes = {}
        self.whiteKnightIndexes = {}
        self.whiteBitshopsIndexes = {}
        self.whiteRooksIndexes = {}
        self.whiteQueenIndexes = {}
        self.whiteKingIndex = {}
        
        #black indexes
        self.blackPawnsIndexes = {}
        self.blackKnightIndexes = {}
        self.blackBitshopsIndexes = {}
        self.blackRooksIndexes = {}
        self.blackQueenIndexes = {}
        self.blackKingIndex = {}
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
            self.blackRooksIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'n'):
            self.nbk = self.nbk.setbit(i)
            self.blackKnightIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'b'):
            self.pbq = self.pbq.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.blackBitshopsIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'q'):
            self.rqk = self.rqk.setbit(i)
            self.pbq = self.pbq.setbit(i)
            self.blackQueenIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'k'):
            self.rqk = self.rqk.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.blackKingIndex[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'p'):
            self.pbq = self.pbq.setbit(i)
            self.blackPawnsIndexes[Utils.getCellBitArrayById(i)] = i
        
        if(pieceType == 'R'):
            self.rqk = self.rqk.setbit(i)
            self.whiteRooksIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'N'):
            self.nbk = self.nbk.setbit(i)
            self.whiteKnightIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'B'):
            self.pbq = self.pbq.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.whiteBitshopsIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'Q'):
            self.rqk = self.rqk.setbit(i)
            self.pbq = self.pbq.setbit(i)
            self.whiteQueenIndexes[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'K'):
            self.rqk = self.rqk.setbit(i)
            self.nbk = self.nbk.setbit(i)
            self.whiteKingIndex[Utils.getCellBitArrayById(i)] = i
        if(pieceType == 'P'):
            self.pbq = self.pbq.setbit(i)
            self.whitePawnsIndexes[Utils.getCellBitArrayById(i)] = i
        return
        
    def setManualConfiguration(self, stringConfig):
        #reset the board
        self.clean()
        
        for i in range(1,64):
            self.setCellbyId(i, stringConfig[i])
        return
    
    def showQuadBoard(self):
        Utils.showBitArray(self.rqk)
        Utils.showBitArray(self.pbq)
        Utils.showBitArray(self.nbk)
        Utils.showBitArray(self.black)
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
        if(view >= 1):
            for i in cells:
                if(i % 8 == 0):
                    output += "\n+------+------+------+------+------+------+------+------+\n"
                    if(i < 8):
                        output = output + "|     0|     1|     2|     3|     4|     5|     6|     7|\n"
                    elif(i < 16):
                        output = output + "|     8|     9|    10|    11|    12|    13|    14|    15|\n"
                    else:
                        for j in range(i,i+8):
                            output = output + "|    "+str(j)
                        output += "|\n"
                if(self.black.getbit(i) == 1):
                    if(blackRooks.getbit(i) == 1):
                        output += "|  r   "
                    elif(blackKnights.getbit(i) == 1):
                        output += "|  n   "
                    elif(blackBitshops.getbit(i) == 1):
                        output += "|   b  "
                    elif(blackPawns.getbit(i) == 1):
                        output += "|  p   "
                    elif(blackQueens.getbit(i) == 1):
                        output += "|  q   "
                    elif(blackKing.getbit(i) == 1):
                        output += "|  k   "
                elif(white.getbit(i) == 1):
                    if(whiteRooks.getbit(i) == 1):
                        output += "|  R   "
                    elif(whiteKnights.getbit(i) == 1):
                        output += "|  N   "
                    elif(whiteBitshops.getbit(i) == 1):
                        output += "|  B   "
                    elif(whitePawns.getbit(i) == 1):
                        output += "|  P   "
                    elif(whiteQueens.getbit(i) == 1):
                        output += "|  Q   "
                    elif(whiteKing.getbit(i) == 1):
                        output += "|  K   "
                else:
                    output += "|      "
                if(i % 8 == 7): 
                    output += "|"
            output += "\n+------+------+------+------+------+------+------+------+\n"
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
        
        #show indexes
        if(view >= 2):
            print "White"
            output = "\tPawn: \t "
            for index in self.whitePawnsIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tKnight:  "
            for index in self.whiteKnightIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tBitshop: "
            for index in self.whiteBitshopsIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tRook: \t "
            for index in self.whiteRooksIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tQueen: \t "
            for index in self.whiteQueenIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tKing: \t "
            for index in self.whiteKingIndex:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            
            if(self.whiteCastleExecuted):
                output += "\n\n\tCastle Executed"
            else:
                output += "\n\n\tCastle Not Executed"
            
            print output
            
            print "\nBlack"
            output = "\tPawn: \t "
            for index in self.blackPawnsIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tKnight:  "
            for index in self.blackKnightIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tBitshop: "
            for index in self.blackBitshopsIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tRook: \t "
            for index in self.blackRooksIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tQueen: \t "
            for index in self.blackQueenIndexes:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            print output
            output = "\tKing: \t "
            for index in self.blackKingIndex:
                output += str(Utils.getPositionByCellBitArray(index)) + "  "
            
            if(self.blackCastleExecuted):
                output += "\n\n\tCastle Executed"
            else:
                output += "\n\n\tCastle Not Executed"
                
            print output
            
        if(view >= 3):
            print "\nHistory:"
            if(self.moveSize > 0):
                for i in range(self.moveSize):
                    print self.moveHistory[i]
            else:
                print "No moves"
        return 
    
    def executeQuietMove(self, move):
        #create bb start/end positions
        cleanBB = ~(move.start | move.end)
        #clean start/end positions
        self.rqk    = self.rqk & cleanBB
        self.pbq    = self.pbq & cleanBB
        self.nbk    = self.nbk & cleanBB
        #set end position
        if(self.black & move.start == move.start):
            #is black piece
            self.black = self.black & ~(move.start | move.end)
            
            #Pawn
            if(move.pieceStart == Constants.PAWN_CODE):
                self.pbq    = self.pbq | move.end
                self.black  = self.black | move.end
                self.blackPawnsIndexes.pop(move.start, None)
                self.blackPawnsIndexes[move.end] = 1 
            #Bitshop
            elif(move.pieceStart == Constants.BITSHOP_CODE):
                self.pbq    = self.pbq | move.end
                self.nbk    = self.nbk | move.end
                self.black  = self.black | move.end
                self.blackBitshopsIndexes.pop(move.start, None)
                self.blackBitshopsIndexes[move.end] = 1
            #Knight
            elif(move.pieceStart == Constants.KNIGHT_CODE):
                self.nbk    = self.nbk | move.end
                self.black  = self.black | move.end
                self.blackKnightIndexes.pop(move.start, None)
                self.blackKnightIndexes[move.end] = 1 
            #Rook
            elif(move.pieceStart == Constants.ROOK_CODE):
                self.rqk    = self.rqk | move.end
                self.black  = self.black | move.end
                self.blackRooksIndexes[move.end] = 1 
                self.blackRooksIndexes.pop(move.start, None)
            #Queen
            elif(move.pieceStart == Constants.QUEEN_CODE):
                self.pbq    = self.pbq | move.end
                self.rqk    = self.rqk | move.end
                self.black  = self.black | move.end
                self.blackQueenIndexes[move.end] = 1 
                self.blackQueenIndexes.pop(move.start, None)
            #King
            else:
                self.rqk    = self.rqk | move.end
                self.nbk    = self.nbk | move.end
                self.black  = self.black | move.end
                self.blackKingIndex[move.end] = 1 
                self.blackKingIndex.pop(move.start, None)
        else:
            #is white piece
                        
            #set end position
            #Pawn
            if(move.pieceStart == Constants.PAWN_CODE):
                self.pbq    = self.pbq | move.end
                self.whitePawnsIndexes[move.end] = 1
                self.whitePawnsIndexes.pop(move.start, None) 
            #Bitshop
            elif(move.pieceStart == Constants.BITSHOP_CODE):
                self.pbq    = self.pbq | move.end
                self.nbk    = self.nbk | move.end
                self.whiteBitshopsIndexes[move.end] = 1 
                self.whiteBitshopsIndexes.pop(move.start, None)
            #Knight
            elif(move.pieceStart == Constants.KNIGHT_CODE):
                self.nbk    = self.nbk | move.end
                self.whiteKnightIndexes[move.end] = 1 
                self.whiteKnightIndexes.pop(move.start, None)
            #Rook
            elif(move.pieceStart == Constants.ROOK_CODE):
                self.rqk    = self.rqk | move.end
                self.whiteRooksIndexes[move.end] = 1 
                self.whiteRooksIndexes.pop(move.start, None)
            #Queen
            elif(move.pieceStart == Constants.QUEEN_CODE):
                self.pbq    = self.pbq | move.end
                self.rqk    = self.rqk | move.end
                self.whiteQueenIndexes[move.end] = 1 
                self.whiteQueenIndexes.pop(move.start, None)
            #King
            else:
                self.rqk    = self.rqk | move.end
                self.nbk    = self.nbk | move.end
                self.whiteKingIndex[move.end] = 1 
                self.whiteKingIndex.pop(move.start, None)
        return
    
    def removeCapturedPiece(self, move):
        if(self.black & move.end == move.end):
            #is black piece
            self.black = self.black & ~(move.start | move.end)
            #detect which Black piece
            #Pawn
            if(self.pbq & ~self.nbk & ~self.rqk & move.end == move.end):
                #remove black pawn
                self.pbq    = self.pbq ^ move.end
                self.blackPawnsIndexes.pop(move.end, None)
            #Bitshop
            elif(self.pbq & self.nbk & ~self.rqk & move.end == move.end):
                #remove black bitshop
                self.pbq    = self.pbq ^ move.end
                self.nbk    = self.nbk ^ move.end
                self.blackBitshopsIndexes.pop(move.end, None)
            #Knight
            elif(~self.pbq & self.nbk & ~self.rqk & move.end == move.end):
                #remove black Knight
                self.nbk    = self.nbk ^ move.end
                self.blackKnightIndexes.pop(move.end, None)
            #Rook
            elif(~self.pbq & ~self.nbk & self.rqk & move.end == move.end):
                #remove black Rook
                self.rqk    = self.rqk ^ move.end
                self.blackRooksIndexes.pop(move.end, None)
            #Queen
            elif(self.pbq & ~self.nbk & self.rqk & move.end == move.end):
                #remove black queen
                self.pbq    = self.pbq ^ move.end
                self.rqk    = self.rqk ^ move.end
                self.blackQueenIndexes.pop(move.end, None) 
            #King
            else:
                #remove black king
                self.nbk    = self.nbk ^ move.end
                self.rqk    = self.rqk ^ move.end
                self.blackKingIndex.pop(move.end, None) 
        else:
            #detect which white piece
            Utils.showBitArray(move.start)
            Utils.showBitArray(move.end)
            #Pawn
            if(self.pbq & ~self.nbk & ~self.rqk & move.end == move.end):
                #remove white pawn
                self.pbq    = self.pbq ^ move.end
                self.whitePawnsIndexes.pop(move.end, None)
            #Bitshop
            elif(self.pbq & self.nbk & ~self.rqk & move.end == move.end):
                #remove white bitshop
                self.pbq    = self.pbq ^ move.end
                self.nbk    = self.nbk ^ move.end
                self.whiteBitshopsIndexes.pop(move.end, None)
            #Knight
            elif(~self.pbq & self.nbk & ~self.rqk & move.end == move.end):
                #remove white Knight
                self.nbk    = self.nbk ^ move.end
                self.whiteKnightIndexes.pop(move.end, None)
            #Rook
            elif(~self.pbq & ~self.nbk & self.rqk & move.end == move.end):
                #remove white Rook
                self.rqk    = self.rqk ^ move.end
                self.whiteRooksIndexes.pop(move.end, None)
            #Queen
            elif(self.pbq & ~self.nbk & self.rqk & move.end == move.end):
                #remove white queen
                self.pbq    = self.pbq ^ move.end
                self.rqk    = self.rqk ^ move.end
                self.whiteQueenIndexes.pop(move.end, None) 
            #King
            else:
                #remove white king
                self.nbk    = self.nbk ^ move.end
                self.rqk    = self.rqk ^ move.end
                self.whiteKingIndex.pop(move.end, None)   
        return
    
    def executeMove(self, move):
        self.moveHistory.append(move)
        self.moveSize += 1
        
        if(move.type == Constants.MOVE_QUIET):
            #quiet move
            self.executeQuietMove(move)
                
        elif(move.type == Constants.MOVE_CAPTURE):
            #capture move     
            #remove captured piece
            self.removeCapturedPiece(move)
            #execute quiet move
            self.executeQuietMove(move)
        
        elif(move.type == Constants.MOVE_DOUBLE_PAWN):
            #double pawn move 
            #execute quiet move
            self.executeQuietMove(move)
                
        elif(move.type == Constants.MOVE_KING_CASTLE):
            if(move.start == Utils.E1):
                self.whiteCastleExecuted = 1
                #white king castle
                self.rqk    = self.rqk ^ Castle.shadowRqkWhiteKingCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkWhiteKingCastle
                #change king position
                self.whiteKingIndex.pop(Utils.E1, None) 
                self.whiteKingIndex[Utils.G1] = 1 
                #change rook position
                self.whiteRooksIndexes.pop(Utils.H1, None) 
                self.whiteRooksIndexes[Utils.F1] = 1 
            else:
                self.blackCastleExecuted = 1
                #black king castle
                self.rqk    = self.rqk ^ Castle.shadowRqkBlackKingCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkBlackKingCastle
                self.black  = self.black ^ Castle.shadowRqkBlackKingCastle
                #change king position
                self.blackKingIndex.pop(Utils.E8, None) 
                self.blackKingIndex[Utils.G8] = 1 
                #change rook position
                self.blackRooksIndexes.pop(Utils.H8, None) 
                self.blackRooksIndexes[Utils.F8] = 1 
                
        elif(move.type == Constants.MOVE_QUEEN_CASTLE):
            if(move.start == Utils.E1):
                self.whiteCastleExecuted = 1
                #white queen castle
                self.rqk    = self.rqk ^ Castle.shadowRqkWhiteQueenCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkWhiteQueenCastle
                #change king position
                self.whiteKingIndex.pop(Utils.E1, None) 
                self.whiteKingIndex[Utils.C1] = 1 
                #change rook position
                self.whiteRooksIndexes.pop(Utils.A1, None) 
                self.whiteRooksIndexes[Utils.D1] = 1 
            else:
                self.blackCastleExecuted = 1
                #black queen castle
                self.rqk    = self.rqk ^ Castle.shadowRqkBlackQueenCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkBlackQueenCastle
                self.black  = self.black ^ Castle.shadowRqkBlackQueenCastle
                #change king position
                self.blackKingIndex.pop(Utils.E8, None) 
                self.blackKingIndex[Utils.C8] = 1 
                #change rook position
                self.blackRooksIndexes.pop(Utils.A8, None) 
                self.blackRooksIndexes[Utils.D8] = 1                 
        
        elif(move.type == Constants.MOVE_EP_CAPTURE):
            #en passant move 
            tmpMove = Move.Move(move.start, EnPassant.getCapturingCellByEndPosition(move.end), Constants.PAWN_CODE, move.type)
            #remove captured piece
            self.removeCapturedPiece(tmpMove)
            #execute quiet move
            self.executeQuietMove(move)
            
        return
    
    def rollbackLastMove(self):
        move = self.moveHistory[self.moveSize-1]
        self.moveSize -= 1
        #print "Last Move: " + str(move)
        
        if(move.type == Constants.MOVE_QUIET):
            #quiet move
            #swap positions for execute reverse quiet move
            tmp = move.start
            move.start = move.end
            move.end = tmp
            #set end position
            self.executeQuietMove(move)
        elif(move.type == Constants.MOVE_CAPTURE):
            #capture move
            #swap positions for execute reverse quiet move
            tmp = move.start
            move.start = move.end
            move.end = tmp
            #set end position
            self.executeQuietMove(move)
            #add captured white piece 
            
            if(move.end & self.black == move.end):
                #capturing piece is black, then captured is white
                #print "capturing piece is black, then captured is white"
                #Pawn
                if(move.pieceEnd == Constants.PAWN_CODE):
                    #print "pawn"
                    self.pbq    = self.pbq | move.start
                    self.whitePawnsIndexes[move.start] = 1
                #Bitshop
                elif(move.pieceEnd == Constants.BITSHOP_CODE):
                    #print "bitshop"
                    self.pbq    = self.pbq | move.start
                    self.nbk    = self.nbk | move.start
                    self.whiteBitshopsIndexes[move.start] = 1 
                #Knight
                elif(move.pieceEnd == Constants.KNIGHT_CODE):
                    #print "knight"
                    self.nbk    = self.nbk | move.start
                    self.whiteKnightIndexes[move.start] = 1 
                #Rook
                elif(move.pieceEnd == Constants.ROOK_CODE):
                    #print "rook"
                    self.rqk    = self.rqk | move.start
                    self.whiteRooksIndexes[move.start] = 1 
                #Queen
                elif(move.pieceEnd == Constants.QUEEN_CODE):
                    #print "queen"
                    self.pbq    = self.pbq | move.start
                    self.rqk    = self.rqk | move.start
                    self.whiteQueenIndexes[move.start] = 1 
                #King
                else:
                    #print "king"
                    self.rqk    = self.rqk | move.start
                    self.nbk    = self.nbk | move.start
                    self.whiteKingIndex[move.start] = 1 
            else:
                #capturing piece is white, then captured is black
                #print "capturing piece is white, then captured is black"
                #Pawn
                if(move.pieceEnd == Constants.PAWN_CODE):
                    #print "pawn"
                    self.pbq    = self.pbq | move.start
                    self.blackPawnsIndexes[move.start] = 1
                #Bitshop
                elif(move.pieceEnd == Constants.BITSHOP_CODE):
                    #print "bitshop"
                    self.pbq    = self.pbq | move.start
                    self.nbk    = self.nbk | move.start
                    self.blackBitshopsIndexes[move.start] = 1 
                #Knight
                elif(move.pieceEnd == Constants.KNIGHT_CODE):
                    #print "knight"
                    self.nbk    = self.nbk | move.start
                    self.blackKnightIndexes[move.start] = 1 
                #Rook
                elif(move.pieceEnd == Constants.ROOK_CODE):
                    #print "rook"
                    self.rqk    = self.rqk | move.start
                    self.blackRooksIndexes[move.start] = 1 
                #Queen
                elif(move.pieceEnd == Constants.QUEEN_CODE):
                    #print "queen"
                    self.pbq    = self.pbq | move.start
                    self.rqk    = self.rqk | move.start
                    self.blackQueenIndexes[move.start] = 1 
                #King
                else:
                    #print "king"
                    self.rqk    = self.rqk | move.start
                    self.nbk    = self.nbk | move.start
                    self.blackKingIndex[move.start] = 1
        elif(move.type == Constants.MOVE_DOUBLE_PAWN):
            #double pawn move
            #swap positions for execute reverse quiet move
            tmp = move.start
            move.start = move.end
            move.end = tmp
            #set end position
            self.executeQuietMove(move)
        elif(move.type == Constants.MOVE_KING_CASTLE):
            if(move.start == Utils.E1):
                self.whiteCastleExecuted = 0
                #white queen castle
                self.rqk    = self.rqk ^ Castle.shadowRqkWhiteKingCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkWhiteKingCastle
                #change king position
                self.whiteKingIndex.pop(Utils.G1, None) 
                self.whiteKingIndex[Utils.E1] = 1 
                #change rook position
                self.whiteRooksIndexes.pop(Utils.F1, None) 
                self.whiteRooksIndexes[Utils.H1] = 1 
            else:
                self.blackCastleExecuted = 0
                #black king castle
                self.rqk    = self.rqk ^ Castle.shadowRqkBlackKingCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkBlackKingCastle
                self.black  = self.black ^ Castle.shadowRqkBlackKingCastle
                #change king position
                self.blackKingIndex.pop(Utils.G8, None) 
                self.blackKingIndex[Utils.E8] = 1 
                #change rook position
                self.blackRooksIndexes.pop(Utils.F8, None) 
                self.blackRooksIndexes[Utils.H8] = 1 
        elif(move.type == Constants.MOVE_QUEEN_CASTLE):
            if(move.start == Utils.E1):
                self.whiteCastleExecuted = 0
                #white queen castle
                self.rqk    = self.rqk ^ Castle.shadowRqkWhiteQueenCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkWhiteQueenCastle
                #change king position
                self.whiteKingIndex.pop(Utils.C1, None) 
                self.whiteKingIndex[Utils.E1] = 1 
                #change rook position
                self.whiteRooksIndexes.pop(Utils.D1, None) 
                self.whiteRooksIndexes[Utils.A1] = 1 
            else:
                self.blackCastleExecuted = 0
                #black queen castle
                self.rqk    = self.rqk ^ Castle.shadowRqkBlackQueenCastle
                self.nbk    = self.nbk ^ Castle.shadowNbkBlackQueenCastle
                self.black  = self.black ^ Castle.shadowRqkBlackQueenCastle
                #change king position
                self.blackKingIndex.pop(Utils.C8, None) 
                self.blackKingIndex[Utils.E8] = 1 
                #change rook position
                self.blackRooksIndexes.pop(Utils.D8, None) 
                self.blackRooksIndexes[Utils.A8] = 1 
                  
        return
    
    def getPieceCode(self, pos):        
        #rooks
        if( self.rqk & ~self.pbq & ~self.nbk & pos == pos):
            return Constants.ROOK_CODE
        #knigths
        if(~self.rqk & ~self.pbq &  self.nbk & pos == pos):
            return Constants.KNIGHT_CODE
        #bitshops
        if( self.pbq &  self.nbk             & pos == pos):
            return Constants.BITSHOP_CODE
        #queens
        if( self.rqk &  self.pbq             & pos == pos):
            return Constants.QUEEN_CODE
        #pawns
        if(~self.rqk &  self.pbq & ~self.nbk & pos == pos):
            return Constants.PAWN_CODE
        #kings
        if( self.rqk &              self.nbk & pos == pos):
            return Constants.KING_CODE
        return Constants.NO_PIECE_CODE
        
    def cellNotAbandoned(self, pos):      
        for i in range(self.moveSize):
            if(self.moveHistory[i].start == pos):
                return False
        return True
