'''
Created on 6/apr/2015

@author: Andrea Martire
'''
import Constants
from pieces import Knight, King, Bitshop, Rook, Queen, Pawn
from model import Move, Castle
import Utils

def getAllPseudoLegalMoves(bb, color):
    
    bb.busyCells = bb.rqk | bb.pbq | bb.nbk
    bb.emptyCells = ~bb.busyCells
    
    if(color == Constants.WHITE):
        #set Black enemies
        enemyCells = bb.black
        #White 
        knightIndexes = bb.whiteKnightIndexes
        kingIndex = bb.whiteKingIndex
        bitshopIndexes = bb.whiteBitshopsIndexes
        rookIndexes = bb.whiteRooksIndexes
        queenIndexes = bb.whiteQueenIndexes
        pawnIndexes = bb.whitePawnsIndexes
    elif(color == Constants.BLACK):
        #set White enemies
        enemyCells = (bb.rqk | bb.pbq | bb.nbk) ^ bb.black
        #Black 
        knightIndexes = bb.blackKnightIndexes
        kingIndex = bb.blackKingIndex
        bitshopIndexes = bb.blackBitshopsIndexes
        rookIndexes = bb.blackRooksIndexes
        queenIndexes = bb.blackQueenIndexes
        pawnIndexes = bb.blackPawnsIndexes
    
    knightMoves = getKnightMoves(bb, enemyCells, knightIndexes)
    kingMoves = getKingMoves(bb, enemyCells, kingIndex, color)
    bitshopMoves = getBitshopMoves(bb, enemyCells, bitshopIndexes)
    rookMoves = getRookMoves(bb, enemyCells, rookIndexes)
    queenMoves = getQueenMoves(bb, enemyCells, queenIndexes)
    pawnMoves = getPawnMoves(bb, enemyCells, pawnIndexes, color)
    
    return knightMoves + kingMoves + bitshopMoves + rookMoves + queenMoves + pawnMoves

def getKnightMoves(bb, enemyCells, knightIndexes):
    movesList = []
    #Knights
    for startPos in knightIndexes:
        #get all moves
        allMoves = Knight.getMovesArray(startPos)
        #for each move
        for destCell in allMoves:
            #if dest cell is busy
            if((bb.busyCells & destCell) == destCell):
                #if enemy piece occupies dest cell
                if((enemyCells & destCell) == destCell):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Constants.KNIGHT_CODE, Move.CAPTURE))
            else:
                #add quiet move
                #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Constants.KNIGHT_CODE, Move.QUIET))
    return movesList

def getKingMoves(bb, enemyCells, kingIndex, color):
    movesList = []
    #Kings
    #todo improve with direct access to startPos
    for startPos in kingIndex:
        #get all moves
        allMoves = King.getMovesArray(startPos)
        #for each move
        for destCell in allMoves:
            #if dest cell is busy
            if((bb.busyCells & destCell) == destCell):
                #if enemy piece occupies dest cell
                if((enemyCells & destCell) == destCell):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Constants.KING_CODE, Move.CAPTURE))
            else:
                #add quiet move
                #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Constants.KING_CODE, Move.QUIET))
    
    #check castle
    if(color == Constants.WHITE and bb.whiteCastleEnabled == 1):
        #king position
        E1 = Utils.getCellBitArrayById(4);
        
        #check king position
        if(bb.rqk & bb.nbk & E1 == E1):
            #rook position for KING CASTLE
            H1 = Utils.getCellBitArrayById(7);
            freeSpacesKing = Castle.spacesWhiteKingCastle()
            
            #check rook position and free spaces between king and rook
            if(bb.rqk & ~bb.pbq & ~bb.nbk & H1 == H1 and freeSpacesKing & bb.emptyCells == freeSpacesKing):
                #king and rook in correct position, spaces free
                #todo check attacked king and free spaces
                #todo ADD KING CASTLE
                print "King Castle: " + str(4) + "-" + str(6)
                movesList.append(Move.Move(E1, Utils.getCellBitArrayById(6), Constants.KING_CODE, Move.KING_CASTLE))
            #rook position for QUEEN CASTLE
            A1 = Utils.getCellBitArrayById(0);
            freeSpacesQueen = Castle.spacesWhiteQueenCastle()
            #check rook position and free spaces between king and rook
            if(bb.rqk & ~bb.pbq & ~bb.nbk & A1 == A1 and freeSpacesQueen & bb.emptyCells == freeSpacesQueen):
                #king and rook in correct position, spaces free
                #todo check attacked king and free spaces
                #todo ADD QUEEN CASTLE
                print "Queen Castle: " + str(4) + "-" + str(2)
                movesList.append(Move.Move(E1, Utils.getCellBitArrayById(2), Constants.KING_CODE, Move.QUEEN_CASTLE))
    elif(color == Constants.BLACK):
        #king position
        E8 = Utils.getCellBitArrayById(60);
        
        #check king position
        if(bb.rqk & bb.nbk & E8 == E8):
            #rook position for KING CASTLE
            H8 = Utils.getCellBitArrayById(63);
            freeSpacesKing = Castle.spacesBlackKingCastle()
            #check rook position and free spaces between king and rook
            if(bb.rqk & ~bb.pbq & ~bb.nbk & H8 == H8 and freeSpacesKing & bb.emptyCells == freeSpacesKing):
                #king and rook in correct position, spaces free
                #todo check attacked king and free spaces
                #todo ADD KING CASTLE
                print "King Castle: " + str(60) + "-" + str(62)
                movesList.append(Move.Move(E8, Utils.getCellBitArrayById(62), Constants.KING_CODE, Move.KING_CASTLE))
            #rook position for QUEEN CASTLE
            A8 = Utils.getCellBitArrayById(56);
            freeSpacesQueen = Castle.spacesBlackQueenCastle()
            #check rook position and free spaces between king and rook
            if(bb.rqk & ~bb.pbq & ~bb.nbk & A8 == A8 and freeSpacesQueen & bb.emptyCells == freeSpacesQueen):
                #king and rook in correct position, spaces free
                #todo check attacked king and free spaces
                #todo ADD QUEEN CASTLE
                print "Queen Castle: " + str(60) + "-" + str(58)
                movesList.append(Move.Move(E8, Utils.getCellBitArrayById(58), Constants.KING_CODE, Move.QUEEN_CASTLE))
        
    return movesList

def getBitshopMoves(bb, enemyCells, bitshopIndexes):
    movesList = []
    for startPos in bitshopIndexes:
        #get all moves
        allMoves = Bitshop.getMovesArray(startPos)
        for direction in (Constants.RIGHT_UP, Constants.LEFT_UP, Constants.LEFT_DOWN, Constants.RIGHT_DOWN):
            #for each move
            i = 0
            while i < len(allMoves[direction]):
                destCell = allMoves[direction][i]
                #if dest cell is busy
                if((bb.busyCells & destCell) == destCell):
                    #stop loop
                    i = 99
                    #if enemy piece occupies dest cell
                    if((enemyCells & destCell) == destCell):
                        #enemy piece. add capture move
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move.Move(startPos, destCell, Constants.BITSHOP_CODE, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Constants.BITSHOP_CODE, Move.QUIET))
                i += 1
    return movesList

def getRookMoves(bb, enemyCells, rookIndexes):
    movesList = []
    for startPos in rookIndexes:
        #get all moves
        allMoves = Rook.getMovesArray(startPos)
        for direction in (Constants.RIGHT, Constants.UP, Constants.LEFT, Constants.DOWN):
            #for each move
            i = 0
            while i < len(allMoves[direction]):
                destCell = allMoves[direction][i]
                #if dest cell is busy
                if((bb.busyCells & destCell) == destCell):
                    #stop loop
                    i = 99
                    #if enemy piece occupies dest cell
                    if((enemyCells & destCell) == destCell):
                        #enemy piece. add capture move
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move.Move(startPos, destCell, Constants.ROOK_CODE, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Constants.ROOK_CODE, Move.QUIET))
                i += 1
    return movesList

def getQueenMoves(bb, enemyCells, queenIndexes):
    movesList = []
    for startPos in queenIndexes:
        #get all moves
        allMoves = Queen.getMovesArray(startPos)
        for direction in (Constants.RIGHT, Constants.RIGHT_UP, Constants.UP, Constants.LEFT_UP, Constants.LEFT, Constants.LEFT_DOWN, Constants.DOWN, Constants.RIGHT_DOWN):
            #for each move
            i = 0
            while i < len(allMoves[direction]):
                destCell = allMoves[direction][i]
                #if dest cell is busy
                if((bb.busyCells & destCell) == destCell):
                    #stop loop
                    i = 99
                    #if enemy piece occupies dest cell
                    if((enemyCells & destCell) == destCell):
                        #enemy piece. add capture move
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move.Move(startPos, destCell, Constants.QUEEN_CODE, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Constants.QUEEN_CODE, Move.QUIET))
                i += 1
    return movesList

def getPawnMoves(bb, enemyCells, pawnIndexes, color):
    movesList = []
    emptyCells = ~bb.busyCells
    for startPos in pawnIndexes:
        #get all moves
        allMoves = Pawn.getMovesArray(startPos, color)
        #move left up
        if Constants.LEFT_UP in allMoves:
            destCell = allMoves[Constants.LEFT_UP]
            #if enemy piece occupies dest cell
            if((enemyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Constants.PAWN_CODE, Move.CAPTURE))
        #move right up
        if Constants.RIGHT_UP in allMoves:
            destCell = allMoves[Constants.RIGHT_UP]
            #if enemy piece occupies dest cell
            if((enemyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Constants.PAWN_CODE, Move.CAPTURE))
        #move up. 1
        if Constants.UP in allMoves:
            destCell = allMoves[Constants.UP]
            #if dest cell is empty
            if((emptyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Constants.PAWN_CODE, Move.QUIET))
        #move up. 2
        if Constants.DOUBLE_UP in allMoves:
            destCellUp = allMoves[Constants.UP]
            destCellDoubleUp = allMoves[Constants.DOUBLE_UP]
            #if cell UP and cell DOUBLE_UP are empty
            if((emptyCells & destCellUp) == destCellUp and (emptyCells & destCellDoubleUp) == destCellDoubleUp):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCellDoubleUp)
                movesList.append(Move.Move(startPos, destCellDoubleUp, Constants.PAWN_CODE, Move.QUIET))
    return movesList