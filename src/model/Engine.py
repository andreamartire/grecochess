'''
Created on 6/apr/2015

@author: Andrea Martire
'''

from pieces import Knight, King, Bitshop, Rook, Queen, Pawn

from model.QuadBitBoard import EMPTY_BIT_BOARD
import Constants
from model.Move import Move
import Utils
from model import Castle

class Engine(object):
    
    @staticmethod
    def getAllPseudoLegalMoves(bb, color, checkCastles):
        
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
        
        knightMoves = Engine.getKnightMoves(bb, enemyCells, knightIndexes)
        bitshopMoves = Engine.getBitshopMoves(bb, enemyCells, bitshopIndexes)
        rookMoves = Engine.getRookMoves(bb, enemyCells, rookIndexes)
        queenMoves = Engine.getQueenMoves(bb, enemyCells, queenIndexes)
        pawnMoves = Engine.getPawnMoves(bb, enemyCells, pawnIndexes, color)
        kingMoves = Engine.getKingMoves(bb, enemyCells, kingIndex, color, checkCastles)
        
        return knightMoves + kingMoves + bitshopMoves + rookMoves + queenMoves + pawnMoves
    
    @staticmethod
    def getKnightMoves(bb, enemyCells, knightIndexes):
        movesList = []
        #Knights
        for startPos in knightIndexes:
            #get all moves
            allMoves = Knight.getMovesArray(startPos)
            #for each move
            for destCell in allMoves:
                #if dest cell is busy
                if(bb.busyCells & destCell == destCell):
                    #if enemy piece occupies dest cell
                    if(enemyCells & destCell == destCell):
                        #enemy piece. add capture move
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.KNIGHT_CODE, Constants.MOVE_CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.KNIGHT_CODE, Constants.MOVE_QUIET))
        return movesList
    
    @staticmethod
    def getKingMoves(bb, enemyCells, kingIndex, color, checkCastles):
        movesList = []
        #Kings
        #todo improve with direct access to startPos
        for startPos in kingIndex:
            #get all moves
            allMoves = King.getMovesArray(startPos)
            #for each move
            for destCell in allMoves:
                #if dest cell is busy
                if(bb.busyCells & destCell == destCell):
                    #if enemy piece occupies dest cell
                    if(enemyCells & destCell == destCell):
                        #enemy piece. add capture move
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.KING_CODE, Constants.MOVE_CAPTURE))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.KING_CODE, Constants.MOVE_QUIET))
        
        #check if castle generation is enabled
        if(checkCastles):
            #check castle
            if(color == Constants.WHITE and bb.whiteCastleEnabled == 1):
                #check king position
                if(bb.rqk & bb.nbk & Utils.E1 == Utils.E1):
                    #check rook position and free spaces between king and rook
                    if(bb.rqk & ~bb.pbq & ~bb.nbk & Utils.H1 == Utils.H1 and Castle.spacesWhiteKingCastle & bb.emptyCells == Castle.spacesWhiteKingCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsWhiteKingCastle & enemyAttacks == EMPTY_BIT_BOARD):
                            print "King Castle: " + str(4) + "-" + str(6)
                            movesList.append(Move(Utils.E1, Utils.getCellBitArrayById(6), Constants.KING_CODE, Constants.MOVE_KING_CASTLE))
                    #check rook position and free spaces between king and rook
                    if(bb.rqk & ~bb.pbq & ~bb.nbk & Utils.A1 == Utils.A1 and Castle.spacesWhiteQueenCastle & bb.emptyCells == Castle.spacesWhiteQueenCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsWhiteQueenCastle & enemyAttacks == EMPTY_BIT_BOARD):
                            print "Queen Castle: " + str(4) + "-" + str(2)
                            movesList.append(Move(Utils.E1, Utils.getCellBitArrayById(2), Constants.KING_CODE, Constants.MOVE_QUEEN_CASTLE))
            elif(color == Constants.BLACK and bb.blackCastleEnabled == 1):
                #check king position
                if(bb.rqk & bb.nbk & Utils.E8 == Utils.E8):
                    #check rook position and free spaces between king and rook
                    if(bb.rqk & ~bb.pbq & ~bb.nbk & Utils.H8 == Utils.H8 and Castle.spacesBlackKingCastle & bb.emptyCells == Castle.spacesBlackKingCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsBlackKingCastle & enemyAttacks == EMPTY_BIT_BOARD):
                            print "King Castle: " + str(60) + "-" + str(62)
                            movesList.append(Move(Utils.E8, Utils.getCellBitArrayById(62), Constants.KING_CODE, Constants.MOVE_KING_CASTLE))
                    #check rook position and free spaces between king and rook
                    if(bb.rqk & ~bb.pbq & ~bb.nbk & Utils.A8 == Utils.A8 and Castle.spacesBlackQueenCastle & bb.emptyCells == Castle.spacesBlackQueenCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsBlackQueenCastle & enemyAttacks == EMPTY_BIT_BOARD):
                            print "Queen Castle: " + str(60) + "-" + str(58)
                            movesList.append(Move(Utils.E8, Utils.getCellBitArrayById(58), Constants.KING_CODE, Constants.MOVE_QUEEN_CASTLE))

                
        return movesList
    
    @staticmethod
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
                    if(bb.busyCells & destCell == destCell):
                        #stop loop
                        i = 99
                        #if enemy piece occupies dest cell
                        if(enemyCells & destCell == destCell):
                            #enemy piece. add capture move
                            #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                            movesList.append(Move(startPos, destCell, Constants.BITSHOP_CODE, Constants.MOVE_CAPTURE))
                    else:
                        #add quiet move
                        #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.BITSHOP_CODE, Constants.MOVE_QUIET))
                    i += 1
        return movesList
    
    @staticmethod
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
                    if(bb.busyCells & destCell == destCell):
                        #stop loop
                        i = 99
                        #if enemy piece occupies dest cell
                        if(enemyCells & destCell == destCell):
                            #enemy piece. add capture move
                            #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                            movesList.append(Move(startPos, destCell, Constants.ROOK_CODE, Constants.MOVE_CAPTURE))
                    else:
                        #add quiet move
                        #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.ROOK_CODE, Constants.MOVE_QUIET))
                    i += 1
        return movesList
    
    @staticmethod
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
                    if(bb.busyCells & destCell == destCell):
                        #stop loop
                        i = 99
                        #if enemy piece occupies dest cell
                        if(enemyCells & destCell == destCell):
                            #enemy piece. add capture move
                            #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                            movesList.append(Move(startPos, destCell, Constants.QUEEN_CODE, Constants.MOVE_CAPTURE))
                    else:
                        #add quiet move
                        #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.QUEEN_CODE, Constants.MOVE_QUIET))
                    i += 1
        return movesList
    
    @staticmethod
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
                if(enemyCells & destCell == destCell):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_CAPTURE))
            #move right up
            if Constants.RIGHT_UP in allMoves:
                destCell = allMoves[Constants.RIGHT_UP]
                #if enemy piece occupies dest cell
                if(enemyCells & destCell == destCell):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_CAPTURE))
            #move up. 1
            if Constants.UP in allMoves:
                destCell = allMoves[Constants.UP]
                #if dest cell is empty
                if(emptyCells & destCell == destCell):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_QUIET))
            #move up. 2
            if Constants.DOUBLE_UP in allMoves:
                destCellUp = allMoves[Constants.UP]
                destCellDoubleUp = allMoves[Constants.DOUBLE_UP]
                #if cell UP and cell DOUBLE_UP are empty
                if(emptyCells & destCellUp == destCellUp and emptyCells & destCellDoubleUp == destCellDoubleUp):
                    #enemy piece. add capture move
                    #print "Capture Move: " + str(startPos) + "-" + str(destCellDoubleUp)
                    movesList.append(Move(startPos, destCellDoubleUp, Constants.PAWN_CODE, Constants.MOVE_QUIET))
        return movesList