'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteKnightTest(unittest.TestCase):
    
    def testWhiteKnightMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
    def testWhiteKnightTakeBlackPawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
            
    def testWhiteKnightTakeBlackKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
            
    def testWhiteKnightTakeBlackBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackBitshopsIndexes
    
    def testWhiteKnightTakeBlackRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackRooksIndexes
    
    def testWhiteKnightTakeBlackQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackQueenIndexes
        
    def testWhiteKnightTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(37, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex
        
    
    def testWhiteKnightMoveUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
    
    def testWhiteKnightTakeBlackPawnUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2        
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackPawnsIndexes
    
    def testWhiteKnightTakeBlackKnightUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
    def testWhiteKnightTakeBlackBitshopUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackBitshopsIndexes
        
    def testWhiteKnightTakeBlackRookUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackRooksIndexes
        
    def testWhiteKnightTakeBlackQueenUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackQueenIndexes
        
    def testWhiteKnightTakeBlackKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(42, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2  
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.blackKingIndex
    
    def testWhiteKnightMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
    
    def testWhiteKnightTakeBlackPawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
    
    def testWhiteKnightTakeBlackKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
    
    def testWhiteKnightTakeBlackBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
        
    def testWhiteKnightTakeBlackRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes
        
    def testWhiteKnightTakeBlackQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
    def testWhiteKnightTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(33, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
    def testWhiteKnightMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
    def testWhiteKnightTakeBlackPawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        
    def testWhiteKnightTakeBlackKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
            
    def testWhiteKnightTakeBlackBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackBitshopsIndexes
            
    def testWhiteKnightTakeBlackRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackRooksIndexes
            
    def testWhiteKnightTakeBlackQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackQueenIndexes
            
    def testWhiteKnightTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(17, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.blackKingIndex
        
    def testWhiteKnightMoveDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
    
    def testWhiteKnightTakeBlackPawnDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackPawnsIndexes
    
    def testWhiteKnightTakeBlackKnightDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
    def testWhiteKnightTakeBlackBitshopDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackBitshopsIndexes
        
    def testWhiteKnightTakeBlackRookDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackRooksIndexes
        
    def testWhiteKnightTakeBlackQueenDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackQueenIndexes
        
    def testWhiteKnightTakeBlackKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(10, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex
        
    def testWhiteKnightMoveDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
    def testWhiteKnightTakeBlackPawnDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackPawnsIndexes
        
    def testWhiteKnightTakeBlackKnightDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
    def testWhiteKnightTakeBlackBitshopDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackBitshopsIndexes
            
    def testWhiteKnightTakeBlackRookDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackRooksIndexes
        
    def testWhiteKnightTakeBlackQueenDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackQueenIndexes
            
    def testWhiteKnightTakeBlackKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(12, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
    
    def testWhiteKnightMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        
    def testWhiteKnightTakeBlackPawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackPawnsIndexes
        
    def testWhiteKnightTakeBlackKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
    def testWhiteKnightTakeBlackBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackBitshopsIndexes
        
    def testWhiteKnightTakeBlackRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackRooksIndexes
        
    def testWhiteKnightTakeBlackQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackQueenIndexes
    
    def testWhiteKnightTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'N')
        board.setCellbyId(21, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.blackKingIndex
    