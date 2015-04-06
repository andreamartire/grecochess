'''
Created on 6/apr/2015

@author: Andrea Martire
'''
import Constants
from pieces import Knight, King, Bitshop, Rook, Queen, Pawn
from model import Move

def getAllPseudoLegalMoves(bb, color):
    
    bb.busyCells = bb.rqk | bb.pbq | bb.nbk
    
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
    kingMoves = getKingMoves(bb, enemyCells, kingIndex)
    bitshopMoves = getBitshopMoves(bb, enemyCells, bitshopIndexes)
    rookMoves = getRookMoves(bb, enemyCells, rookIndexes)
    queenMoves = getQueenMoves(bb, enemyCells, queenIndexes)
    pawnMoves = getPawnMoves(bb, enemyCells, pawnIndexes, color)
    
    return

def getKnightMoves(bb, enemyCells, knightIndexes):
    movesList = []
    #White Knights
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
                    movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
            else:
                #add quiet move
                #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Move.QUIET))
    return movesList

def getKingMoves(bb, enemyCells, kingIndex):
    movesList = []
    #get all moves
    allMoves = King.getMovesArray(kingIndex)
    #for each move
    for destCell in allMoves:
        #if dest cell is busy
        if((bb.busyCells & destCell) == destCell):
            #if enemy piece occupies dest cell
            if((enemyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(kingIndex) + "-" + str(destCell)
                movesList.append(Move.Move(kingIndex, destCell, Move.CAPTURE))
        else:
            #add quiet move
            #print "Quiet Move: " + str(kingIndex) + "-" + str(destCell)
            movesList.append(Move.Move(kingIndex, destCell, Move.QUIET))
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
                        movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Move.QUIET))
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
                        movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Move.QUIET))
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
                        movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move.Move(startPos, destCell, Move.QUIET))
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
                movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
        #move right up
        if Constants.RIGHT_UP in allMoves:
            destCell = allMoves[Constants.RIGHT_UP]
            #if enemy piece occupies dest cell
            if((enemyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Move.CAPTURE))
        #move up. 1
        if Constants.UP in allMoves:
            destCell = allMoves[Constants.UP]
            #if dest cell is empty
            if((emptyCells & destCell) == destCell):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                movesList.append(Move.Move(startPos, destCell, Move.QUIET))
        #move up. 2
        if Constants.DOUBLE_UP in allMoves:
            destCellUp = allMoves[Constants.UP]
            destCellDoubleUp = allMoves[Constants.DOUBLE_UP]
            #if cell UP and cell DOUBLE_UP are empty
            if((emptyCells & destCellUp) == destCellUp and (emptyCells & destCellDoubleUp) == destCellDoubleUp):
                #enemy piece. add capture move
                #print "Capture Move: " + str(startPos) + "-" + str(destCellDoubleUp)
                movesList.append(Move.Move(startPos, destCellDoubleUp, Move.QUIET))
    return movesList