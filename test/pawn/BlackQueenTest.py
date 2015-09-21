'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteQueenTest(unittest.TestCase):
    
    def testBlackQueenMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
            
    def testBlackQueenTakeWhiteKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
            
    def testBlackQueenTakeWhiteBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
    
    def testBlackQueenTakeWhiteRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
    
    def testBlackQueenTakeWhiteQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
    def testBlackQueenTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(36, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
    
    def testBlackQueenMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
    def testBlackQueenTakeWhiteKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
            
    def testBlackQueenTakeWhiteBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
            
    def testBlackQueenTakeWhiteRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
            
    def testBlackQueenTakeWhiteQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
            
    def testBlackQueenTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(18, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
    
    def testBlackQueenMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
    def testBlackQueenTakeWhiteKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
    def testBlackQueenTakeWhiteBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
    def testBlackQueenTakeWhiteRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
    def testBlackQueenTakeWhiteQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
    
    def testBlackQueenTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(20, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
    
    def testBlackQueenMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
    
    def testBlackQueenTakeWhitePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
    
    def testBlackQueenTakeWhiteKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
    
    def testBlackQueenTakeWhiteBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
    def testBlackQueenTakeWhiteRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
    def testBlackQueenTakeWhiteQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
    def testBlackQueenTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(34, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
    
    def testBlackQueenMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
            
    def testBlackQueenTakeWhiteKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
            
    def testBlackQueenTakeWhiteBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
    
    def testBlackQueenTakeWhiteRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
    
    def testBlackQueenTakeWhiteQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
    def testBlackQueenTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(28, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
    
    def testBlackQueenMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
    def testBlackQueenTakeWhiteKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
            
    def testBlackQueenTakeWhiteBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
            
    def testBlackQueenTakeWhiteRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
            
    def testBlackQueenTakeWhiteQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
            
    def testBlackQueenTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(26, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
    
    def testBlackQueenMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
    def testBlackQueenTakeWhitePawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
    def testBlackQueenTakeWhiteKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
    def testBlackQueenTakeWhiteBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
    def testBlackQueenTakeWhiteRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
    def testBlackQueenTakeWhiteQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
    
    def testBlackQueenTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(19, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackQueenMoveUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
    
    def testBlackQueenTakeWhitePawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
    
    def testBlackQueenTakeWhiteKnightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
    
    def testBlackQueenTakeWhiteBitshopUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
    def testBlackQueenTakeWhiteRookUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
    def testBlackQueenTakeWhiteQueenUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
    def testBlackQueenTakeWhiteKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'q')
        board.setCellbyId(35, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
    