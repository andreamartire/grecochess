'''
Created on 14/apr/2015

@author: Andrea Martire
'''
from gmpy import mpz
import Utils
from model import QuadBitBoard
import Constants
from model.Move import Move, KING_CASTLE, QUEEN_CASTLE

#white
#king side
spacesWhiteKingCastle = mpz(0).setbit(5).setbit(6)
safeCellsWhiteKingCastle = mpz(0).setbit(4).setbit(5).setbit(6)
#queen side
spacesWhiteQueenCastle = mpz(0).setbit(3).setbit(2).setbit(1)
safeCellsWhiteQueenCastle = mpz(0).setbit(4).setbit(3).setbit(2)

#black
#king side
spacesBlackKingCastle = mpz(0).setbit(61).setbit(62)
safeCellsBlackKingCastle = mpz(0).setbit(60).setbit(61).setbit(62)
#queen side
spacesBlackQueenCastle = mpz(0).setbit(59).setbit(58).setbit(57)
safeCellsBlackQueenCastle = mpz(0).setbit(60).setbit(59).setbit(58)

def generateBlackCastles(bb, movesList):
    #king position
    E8 = Utils.getCellBitArrayById(60);
    
    #check king position
    if(bb.rqk & bb.nbk & E8 == E8):
        #rook position for KING CASTLE
        H8 = Utils.getCellBitArrayById(63);
        #check rook position and free spaces between king and rook
        if(bb.rqk & ~bb.pbq & ~bb.nbk & H8 == H8 and spacesBlackKingCastle & bb.emptyCells == spacesBlackKingCastle):
            #king and rook in correct position, spaces free
            from model.Engine import Engine
            #get all enemy moves
            enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
            #check if king is attacked king and free spaces
            enemyAttacks = QuadBitBoard.EMPTY_BIT_BOARD
            for move in enemyMoves:
                enemyAttacks |= move.end
            #if king and white spaces aren't under attack
            if(safeCellsBlackKingCastle & enemyAttacks == QuadBitBoard.EMPTY_BIT_BOARD):
                print "King Castle: " + str(60) + "-" + str(62)
                movesList.append(Move(E8, Utils.getCellBitArrayById(62), Constants.KING_CODE, KING_CASTLE))
        #rook position for QUEEN CASTLE
        A8 = Utils.getCellBitArrayById(56);
        #check rook position and free spaces between king and rook
        if(bb.rqk & ~bb.pbq & ~bb.nbk & A8 == A8 and spacesBlackQueenCastle & bb.emptyCells == spacesBlackQueenCastle):
            #king and rook in correct position, spaces free
            #get all enemy moves
            enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.WHITE, False)
            #check if king is attacked king and free spaces
            enemyAttacks = QuadBitBoard.EMPTY_BIT_BOARD
            for move in enemyMoves:
                enemyAttacks |= move.end
            #if king and white spaces aren't under attack
            if(safeCellsBlackQueenCastle & enemyAttacks == QuadBitBoard.EMPTY_BIT_BOARD):
                print "Queen Castle: " + str(60) + "-" + str(58)
                movesList.append(Move(E8, Utils.getCellBitArrayById(58), Constants.KING_CODE, QUEEN_CASTLE))

def generateWhiteCastles(bb, movesList):
    #king position
    E1 = Utils.getCellBitArrayById(4);
    
    #check king position
    if(bb.rqk & bb.nbk & E1 == E1):
        #rook position for KING CASTLE
        H1 = Utils.getCellBitArrayById(7);
        #check rook position and free spaces between king and rook
        if(bb.rqk & ~bb.pbq & ~bb.nbk & H1 == H1 and spacesWhiteKingCastle & bb.emptyCells == spacesWhiteKingCastle):
            #king and rook in correct position, spaces free
            from model.Engine import Engine
            #get all enemy moves
            enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
            #check if king is attacked king and free spaces
            enemyAttacks = QuadBitBoard.EMPTY_BIT_BOARD
            for move in enemyMoves:
                enemyAttacks |= move.end
            #if king and white spaces aren't under attack
            if(safeCellsWhiteKingCastle & enemyAttacks == QuadBitBoard.EMPTY_BIT_BOARD):
                print "King Castle: " + str(4) + "-" + str(6)
                movesList.append(Move(E1, Utils.getCellBitArrayById(6), Constants.KING_CODE, KING_CASTLE))
        #rook position for QUEEN CASTLE
        A1 = Utils.getCellBitArrayById(0);
        #check rook position and free spaces between king and rook
        if(bb.rqk & ~bb.pbq & ~bb.nbk & A1 == A1 and spacesWhiteQueenCastle & bb.emptyCells == spacesWhiteQueenCastle):
            #king and rook in correct position, spaces free
            #get all enemy moves
            enemyMoves = Engine.getAllPseudoLegalMoves(bb, Constants.BLACK, False)
            #check if king is attacked king and free spaces
            enemyAttacks = QuadBitBoard.EMPTY_BIT_BOARD
            for move in enemyMoves:
                enemyAttacks |= move.end
            #if king and white spaces aren't under attack
            if(safeCellsWhiteQueenCastle & enemyAttacks == QuadBitBoard.EMPTY_BIT_BOARD):
                print "Queen Castle: " + str(4) + "-" + str(2)
                movesList.append(Move(E1, Utils.getCellBitArrayById(2), Constants.KING_CODE, QUEEN_CASTLE))
