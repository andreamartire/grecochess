'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class BlackBitshopTest(unittest.TestCase):
    
    def testBlackBitshopMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
    def testBlackBitshopTakeWhitePawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
            
    def testBlackBitshopTakeWhiteKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKnightIndexes
            
    def testBlackBitshopTakeWhiteBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
    
    def testBlackBitshopTakeWhiteRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteRooksIndexes
    
    def testBlackBitshopTakeWhiteQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
    def testBlackBitshopTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(36, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
    
    def testBlackBitshopMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
    def testBlackBitshopTakeWhitePawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whitePawnsIndexes
        
    def testBlackBitshopTakeWhiteKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKnightIndexes
            
    def testBlackBitshopTakeWhiteBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
            
    def testBlackBitshopTakeWhiteRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteRooksIndexes
            
    def testBlackBitshopTakeWhiteQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
            
    def testBlackBitshopTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(18, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
    
    def testBlackBitshopMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
    def testBlackBitshopTakeWhitePawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whitePawnsIndexes
        
    def testBlackBitshopTakeWhiteKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes
        
    def testBlackBitshopTakeWhiteBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
    def testBlackBitshopTakeWhiteRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteRooksIndexes
        
    def testBlackBitshopTakeWhiteQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
    
    def testBlackBitshopTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(20, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
    
    def testBlackBitshopMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
    
    def testBlackBitshopTakeWhitePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whitePawnsIndexes
    
    def testBlackBitshopTakeWhiteKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKnightIndexes
    
    def testBlackBitshopTakeWhiteBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
    def testBlackBitshopTakeWhiteRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteRooksIndexes
        
    def testBlackBitshopTakeWhiteQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
    def testBlackBitshopTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'b')
        board.setCellbyId(34, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
    