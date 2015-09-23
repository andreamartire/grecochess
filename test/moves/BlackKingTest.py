'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class BlackKingTest(unittest.TestCase):
    
    def testBlackKingMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
            
    def testBlackKingTakeWhiteKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
            
    def testBlackKingTakeWhiteBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
    
    def testBlackKingTakeWhiteRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
    
    def testBlackKingTakeWhiteQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
    def testBlackKingTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(36, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
    
    def testBlackKingMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
    def testBlackKingTakeWhiteKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
            
    def testBlackKingTakeWhiteBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
            
    def testBlackKingTakeWhiteRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
            
    def testBlackKingTakeWhiteQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
            
    def testBlackKingTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(18, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
    
    def testBlackKingMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
    def testBlackKingTakeWhiteKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
    def testBlackKingTakeWhiteBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
    def testBlackKingTakeWhiteRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
    def testBlackKingTakeWhiteQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
    
    def testBlackKingTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(20, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
    
    def testBlackKingMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
    
    def testBlackKingTakeWhitePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
    
    def testBlackKingTakeWhiteKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
    
    def testBlackKingTakeWhiteBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
    def testBlackKingTakeWhiteRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
    def testBlackKingTakeWhiteQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
    def testBlackKingTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(34, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
    
    def testBlackKingMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
            
    def testBlackKingTakeWhiteKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
            
    def testBlackKingTakeWhiteBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
    
    def testBlackKingTakeWhiteRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
    
    def testBlackKingTakeWhiteQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
    def testBlackKingTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(28, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
    
    def testBlackKingMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
    def testBlackKingTakeWhiteKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
            
    def testBlackKingTakeWhiteBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
            
    def testBlackKingTakeWhiteRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
            
    def testBlackKingTakeWhiteQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
            
    def testBlackKingTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(26, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
    
    def testBlackKingMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testBlackKingTakeWhitePawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
    def testBlackKingTakeWhiteKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
    def testBlackKingTakeWhiteBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
    def testBlackKingTakeWhiteRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
    def testBlackKingTakeWhiteQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
    
    def testBlackKingTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(19, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackKingMoveUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
    
    def testBlackKingTakeWhitePawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
    
    def testBlackKingTakeWhiteKnightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
    
    def testBlackKingTakeWhiteBitshopUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
    def testBlackKingTakeWhiteRookUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
    def testBlackKingTakeWhiteQueenUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
    def testBlackKingTakeWhiteKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'k')
        board.setCellbyId(35, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
    
    def testBlackKingMoveKingCastle(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(60, 'k')
        board.setCellbyId(63, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        assert Utils.getCellBitArrayById(63) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 60, 62)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(62) in board.blackKingIndex
        assert Utils.getCellBitArrayById(61) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        assert Utils.getCellBitArrayById(63) in board.blackRooksIndexes
    
    def testBlackKingMoveQueenCastle(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(60, 'k')
        board.setCellbyId(56, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        assert Utils.getCellBitArrayById(56) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 60, 58)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(58) in board.blackKingIndex
        assert Utils.getCellBitArrayById(59) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(60) in board.blackKingIndex
        assert Utils.getCellBitArrayById(56) in board.blackRooksIndexes