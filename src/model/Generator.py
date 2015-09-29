'''
Created on 6/apr/2015

@author: Andrea Martire
'''

from pieces import Knight, King, Bitshop, Rook, Queen, Pawn

import Constants
from model.Move import Move
import Utils
from model import Castle, EnPassant
import random
from model.MoveCache import MoveCache

class Generator(object):
    
    cacheReuseCounter = 0
    cacheAddCounter = 0
    
    @staticmethod
    def getMoveByIndexes(bb, color, startCell, endCell):
            
        moves = Generator.getAllPseudoLegalMoves(bb, color, True)
        for move in moves:
            if(move.start == Utils.getCellBitArrayById(startCell) and
               move.end == Utils.getCellBitArrayById(endCell)):
                return move
        return None
    
    
    @staticmethod
    def getPromotionMoveByIndexes(bb, color, startCell, endCell, promotionType):
            
        moves = Generator.getAllPseudoLegalMoves(bb, color, True)
        for move in moves:
            if(move.start == Utils.getCellBitArrayById(startCell) and
               move.end == Utils.getCellBitArrayById(endCell) and 
               move.type == promotionType):
                return move
        return None
    
    @staticmethod
    def getAllPseudoLegalMoves(bb, color, checkCastles=True):            
        #check if exists in move cache
        allMoves = MoveCache.get(color, bb.getHash())
        
        if(allMoves != None):
            Generator.cacheReuseCounter += 1
            return allMoves
        
        Generator.cacheAddCounter += 1
        
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
            
        knightMoves = Generator.getKnightMoves(bb, enemyCells, knightIndexes)
        bitshopMoves = Generator.getBitshopMoves(bb, enemyCells, bitshopIndexes)
        rookMoves = Generator.getRookMoves(bb, enemyCells, rookIndexes)
        queenMoves = Generator.getQueenMoves(bb, enemyCells, queenIndexes)
        pawnMoves = Generator.getPawnMoves(bb, enemyCells, pawnIndexes, color)
        kingMoves = Generator.getKingMoves(bb, enemyCells, kingIndex, color, checkCastles)
            
        allMoves = knightMoves + kingMoves + bitshopMoves + rookMoves + queenMoves + pawnMoves
        
        #order moves
        allMoves = Generator.quicksort(allMoves)
        
        #save moves in cache
        MoveCache.put(color, bb, allMoves)
        
        return allMoves
    
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
                        movesList.append(Move(startPos, destCell, Constants.KNIGHT_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
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
                        movesList.append(Move(startPos, destCell, Constants.KING_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
                else:
                    #add quiet move
                    #print "Quiet Move: " + str(startPos) + "-" + str(destCell)
                    movesList.append(Move(startPos, destCell, Constants.KING_CODE, Constants.MOVE_QUIET))
        
        #check if castle generation is enabled
        if(checkCastles):
            #check castle
            if(color == Constants.WHITE):
                #check king position
                if(bb.rqk & bb.nbk & Utils.E1 == Utils.E1):
                    #check rook position and free spaces between king and rook
                    if(bb.whiteKingCastleRight == 1 and bb.rqk & ~bb.pbq & ~bb.nbk & Utils.H1 == Utils.H1 and Castle.spacesWhiteKingCastle & bb.emptyCells == Castle.spacesWhiteKingCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Generator.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = Utils.EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsWhiteKingCastle & enemyAttacks == Utils.EMPTY_BIT_BOARD and
                                bb.cellNotAbandoned(Utils.E1) and bb.cellNotAbandoned(Utils.H1)):
                            #print "King Castle: " + str(4) + "-" + str(6)
                            movesList.append(Move(Utils.E1, Utils.getCellBitArrayById(6), Constants.KING_CODE, Constants.MOVE_KING_CASTLE))
                    #check rook position and free spaces between king and rook
                    if(bb.whiteQueenCastleRight == 1 and bb.rqk & ~bb.pbq & ~bb.nbk & Utils.A1 == Utils.A1 and Castle.spacesWhiteQueenCastle & bb.emptyCells == Castle.spacesWhiteQueenCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Generator.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = Utils.EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsWhiteQueenCastle & enemyAttacks == Utils.EMPTY_BIT_BOARD and
                                bb.cellNotAbandoned(Utils.E1) and bb.cellNotAbandoned(Utils.A1)):
                            #print "Queen Castle: " + str(4) + "-" + str(2)
                            movesList.append(Move(Utils.E1, Utils.getCellBitArrayById(2), Constants.KING_CODE, Constants.MOVE_QUEEN_CASTLE))
            elif(color == Constants.BLACK):
                #check king position
                if(bb.rqk & bb.nbk & Utils.E8 == Utils.E8):
                    #check rook position and free spaces between king and rook
                    if(bb.blackKingCastleRight == 1 and bb.rqk & ~bb.pbq & ~bb.nbk & Utils.H8 == Utils.H8 and Castle.spacesBlackKingCastle & bb.emptyCells == Castle.spacesBlackKingCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Generator.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = Utils.EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsBlackKingCastle & enemyAttacks == Utils.EMPTY_BIT_BOARD and
                                bb.cellNotAbandoned(Utils.E8) and bb.cellNotAbandoned(Utils.H8)):
                            #print "King Castle: " + str(60) + "-" + str(62)
                            movesList.append(Move(Utils.E8, Utils.getCellBitArrayById(62), Constants.KING_CODE, Constants.MOVE_KING_CASTLE))
                    #check rook position and free spaces between king and rook
                    if(bb.blackQueenCastleRight == 1 and bb.rqk & ~bb.pbq & ~bb.nbk & Utils.A8 == Utils.A8 and Castle.spacesBlackQueenCastle & bb.emptyCells == Castle.spacesBlackQueenCastle):
                        #king and rook in correct position, spaces free
                        #get all enemy moves
                        enemyMoves = Generator.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
                        #check if king is attacked king and free spaces
                        enemyAttacks = Utils.EMPTY_BIT_BOARD
                        for move in enemyMoves:
                            enemyAttacks |= move.end
                        #if king and white spaces aren't under attack
                        if(Castle.safeCellsBlackQueenCastle & enemyAttacks == Utils.EMPTY_BIT_BOARD and
                                bb.cellNotAbandoned(Utils.E8) and bb.cellNotAbandoned(Utils.A8)):
                            #print "Queen Castle: " + str(60) + "-" + str(58)
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
                            movesList.append(Move(startPos, destCell, Constants.BITSHOP_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
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
                            movesList.append(Move(startPos, destCell, Constants.ROOK_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
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
                            movesList.append(Move(startPos, destCell, Constants.QUEEN_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
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
                    if(destCell & Utils.PROMOTION_ROWS == destCell):
                        #capture promotion
                        #print "Promotion Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_QUEEN_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_ROOK_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_BITSHOP_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_KNIGHT_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                    else:    
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
            #move right up
            if Constants.RIGHT_UP in allMoves:
                destCell = allMoves[Constants.RIGHT_UP]
                #if enemy piece occupies dest cell
                if(enemyCells & destCell == destCell):
                    #enemy piece. add capture move
                    if(destCell & Utils.PROMOTION_ROWS == destCell):
                        #capture promotion
                        #print "Promotion Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_QUEEN_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_ROOK_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_BITSHOP_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_KNIGHT_PROMO_CAPTURE, bb.getPieceCode(destCell)))
                    else:    
                        #print "Capture Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_CAPTURE, bb.getPieceCode(destCell)))
            #move up. 1
            if Constants.UP in allMoves:
                destCell = allMoves[Constants.UP]
                #if dest cell is empty
                if(emptyCells & destCell == destCell):
                    #enemy piece. add quiet move
                    if(destCell & Utils.PROMOTION_ROWS == destCell):
                        #promotion
                        #print "Promotion Move: " + str(startPos) + "-" + str(destCell)
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_QUEEN_PROMOTION, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_ROOK_PROMOTION, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_KNIGHT_PROMOTION, bb.getPieceCode(destCell)))
                        movesList.append(Move(startPos, destCell, Constants.PAWN_CODE, Constants.MOVE_BITSHOP_PROMOTION, bb.getPieceCode(destCell)))
                    else:    
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
                    movesList.append(Move(startPos, destCellDoubleUp, Constants.PAWN_CODE, Constants.MOVE_DOUBLE_PAWN))
            #en passant
            #if double push column is setted
            if(bb.doublePushColumn != EnPassant.noDoublePushColumn
               and ((color == Constants.WHITE and startPos & EnPassant.whiteEnPassantRow == startPos) or
                    (color == Constants.BLACK and startPos & EnPassant.blackEnPassantRow == startPos))):
                #get last move
                lastMove = bb.moveHistory[bb.moveSize-1]
                if(lastMove.type == Constants.MOVE_DOUBLE_PAWN):
                    #check left side pawn
                    leftEpBlock = EnPassant.getLeftEnPassantBlock(startPos)
                    if(lastMove.end & leftEpBlock == lastMove.end):
                        movesList.append(Move(startPos, lastMove.end ^ leftEpBlock, Constants.PAWN_CODE, Constants.MOVE_EP_CAPTURE))
                    else:
                        #check right side pawn
                        rightEpBlock = EnPassant.getRightEnPassantBlock(startPos)
                        if(lastMove.end & rightEpBlock == lastMove.end):
                            movesList.append(Move(startPos, lastMove.end ^ rightEpBlock, Constants.PAWN_CODE, Constants.MOVE_EP_CAPTURE))
        
        return movesList
    
    @staticmethod
    def sub_partition(array, start, end, idx_pivot):
        'returns the position where the pivot winds up'
        if not (start <= idx_pivot <= end):
            raise ValueError('idx pivot must be between start and end')
    
        array[start], array[idx_pivot] = array[idx_pivot], array[start]
        pivot = array[start]
        i = start + 1
        j = start + 1
    
        while j <= end:
            #killer move priority
            if array[j].type < pivot.type:
                array[j], array[i] = array[i], array[j]
                i += 1
            #TODO Ahead move priority. Need piece colour
            j += 1
    
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1
    
    @staticmethod
    def quicksort(array, start=0, end=None):
    
        if end is None:
            end = len(array) - 1
    
        if end - start < 1:
            return []
    
        idx_pivot = random.randint(start, end)
        i = Generator.sub_partition(array, start, end, idx_pivot)
        #print array, i, idx_pivot
        Generator.quicksort(array, start, i - 1)
        Generator.quicksort(array, i + 1, end)
        return array