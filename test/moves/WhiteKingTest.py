'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteKingTest(unittest.TestCase):
    
    def testWhiteKingMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
            
    def testWhiteKingTakeBlackKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
            
    def testWhiteKingTakeBlackBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
    
    def testWhiteKingTakeBlackRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
    
    def testWhiteKingTakeBlackQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
    def testWhiteKingTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(36, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
    
    def testWhiteKingMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
    def testWhiteKingTakeBlackKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
            
    def testWhiteKingTakeBlackBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
            
    def testWhiteKingTakeBlackRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
            
    def testWhiteKingTakeBlackQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
            
    def testWhiteKingTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(18, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
    
    def testWhiteKingMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
    def testWhiteKingTakeBlackKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
    def testWhiteKingTakeBlackBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
    def testWhiteKingTakeBlackRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
    def testWhiteKingTakeBlackQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
    
    def testWhiteKingTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(20, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
    
    def testWhiteKingMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
    
    def testWhiteKingTakeBlackPawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
    
    def testWhiteKingTakeBlackKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
    
    def testWhiteKingTakeBlackBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
    def testWhiteKingTakeBlackRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
    def testWhiteKingTakeBlackQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
    def testWhiteKingTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(34, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
    
    def testWhiteKingMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
            
    def testWhiteKingTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
            
    def testWhiteKingTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
    
    def testWhiteKingTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
    
    def testWhiteKingTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
    def testWhiteKingTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(28, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
    
    def testWhiteKingMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
    def testWhiteKingTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
            
    def testWhiteKingTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
            
    def testWhiteKingTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
            
    def testWhiteKingTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
            
    def testWhiteKingTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(26, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
    
    def testWhiteKingMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testWhiteKingTakeBlackPawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
    def testWhiteKingTakeBlackKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
    def testWhiteKingTakeBlackBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
    def testWhiteKingTakeBlackRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
    def testWhiteKingTakeBlackQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
    
    def testWhiteKingTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(19, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
    
    def testWhiteKingMoveUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
    
    def testWhiteKingTakeBlackPawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
    
    def testWhiteKingTakeBlackKnightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
    
    def testWhiteKingTakeBlackBitshopUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
    def testWhiteKingTakeBlackRookUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
    def testWhiteKingTakeBlackQueenUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
    def testWhiteKingTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'K')
        board.setCellbyId(35, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
    def testWhiteKingMoveKingCastle(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(4, 'K')
        board.setCellbyId(7, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(7) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 4, 6)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(6) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(5) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(7) in board.whiteRooksIndexes
    
    def testWhiteKingMoveQueenCastle(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.showBoard(2)
        board.setCellbyId(4, 'K')
        board.setCellbyId(0, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(0) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 4, 2)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(3) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        assert Utils.getCellBitArrayById(0) in board.whiteRooksIndexes
    