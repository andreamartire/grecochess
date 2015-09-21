'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhitePawnTest(unittest.TestCase):
    
    def testWhitePawnTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
    
    def testWhitePawnTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
    
    def testWhitePawnTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
    
    def testWhitePawnTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
    
    def testWhitePawnTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
    
    def testWhitePawnTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
    
    def testWhitePawnTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
    
    def testWhitePawnTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes

    def testWhitePawnTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
    
    def testWhitePawnTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
    def testWhitePawnTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    
    def testWhitePawnTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
    def testWhitePawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(34, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 34)
        
        assert move == None         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
    def testWhitePawnSinglePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 19)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
    
    def testWhitePawnDoublePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 27)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
    def testWhiteEnPassantLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(36, 'P')
        board.setCellbyId(51, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 35)
           
        board.executeMove(move)        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 36, 43)
           
        board.executeMove(move)
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(43) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackPawnsIndexes
         
        board.rollbackLastMove()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes 
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
           
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
    
    def testWhiteEnPassantRight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(36, 'P')
        board.setCellbyId(53, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 53, 37)
           
        board.executeMove(move)        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 36, 45)
           
        board.executeMove(move)
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(45) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) not in board.blackPawnsIndexes
         
        board.rollbackLastMove()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes 
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
           
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) in board.blackPawnsIndexes
    
    def testWhitePromotionToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 59, Constants.MOVE_KNIGHT_PROMOTION)
        
        board.executeMove(move)
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(59) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
    
    def testWhitePromotionToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 59, Constants.MOVE_BITSHOP_PROMOTION)
        
        board.executeMove(move)
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(59) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
    
    def testWhitePromotionToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 59, Constants.MOVE_ROOK_PROMOTION)
        
        board.executeMove(move)
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(59) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
    
    def testWhitePromotionToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 59, Constants.MOVE_QUEEN_PROMOTION)
        
        board.executeMove(move)
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(59) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
      
    def testWhitePromotionCaptureQueenLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(58, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 58, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
    
    def testWhitePromotionCaptureQueenRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackQueenIndexes
      
    def testWhitePromotionCaptureRookRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackRooksIndexes
      
    def testWhitePromotionCaptureBitshopRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'b')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackBitshopsIndexes
      
    def testWhitePromotionCaptureKnightRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'n')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKnightIndexes
          
    def testWhitePromotionCaptureKingRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(51, 'P')
        board.setCellbyId(60, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.WHITE, 51, 60, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(51) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex