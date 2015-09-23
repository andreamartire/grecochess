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
    
    def testBlackKnightMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
    def testBlackKnightTakeWhitePawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whitePawnsIndexes
            
    def testBlackKnightTakeWhiteKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes
            
    def testBlackKnightTakeWhiteBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteBitshopsIndexes
    
    def testBlackKnightTakeWhiteRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteRooksIndexes
    
    def testBlackKnightTakeWhiteQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteQueenIndexes
        
    def testBlackKnightTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(37, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 37)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex
        
    def testBlackKnightMoveUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
    def testBlackKnightTakeWhitePawnUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whitePawnsIndexes
        
    def testBlackKnightTakeWhiteKnightUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteKnightIndexes 
        
    def testBlackKnightTakeWhiteBitshopUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteBitshopsIndexes
        
    def testBlackKnightTakeWhiteRookUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteQueenIndexes
    
    def testBlackKnightTakeWhiteKingUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(44, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 44)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(44) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
    
    def testBlackKnightMoveUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
    
    def testBlackKnightTakeWhitePawnUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2        
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whitePawnsIndexes
    
    def testBlackKnightTakeWhiteKnightUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteKnightIndexes
        
    def testBlackKnightTakeWhiteBitshopUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteBitshopsIndexes
        
    def testBlackKnightTakeWhiteRookUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteQueenIndexes
        
    def testBlackKnightTakeWhiteKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(42, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 42)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(42) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2  
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(42) in board.whiteKingIndex
    
    def testBlackKnightMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
    
    def testBlackKnightTakeWhitePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
    
    def testBlackKnightTakeWhiteKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteKnightIndexes
    
    def testBlackKnightTakeWhiteBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteBitshopsIndexes
        
    def testBlackKnightTakeWhiteRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteQueenIndexes
        
    def testBlackKnightTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(33, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 33)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(33) in board.whiteKingIndex
        
    def testBlackKnightMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
    def testBlackKnightTakeWhitePawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whitePawnsIndexes
        
    def testBlackKnightTakeWhiteKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
            
    def testBlackKnightTakeWhiteBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteBitshopsIndexes
            
    def testBlackKnightTakeWhiteRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteRooksIndexes
            
    def testBlackKnightTakeWhiteQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteQueenIndexes
            
    def testBlackKnightTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(17, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(17) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
        
    def testBlackKnightMoveDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
    
    def testBlackKnightTakeWhitePawnDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whitePawnsIndexes
    
    def testBlackKnightTakeWhiteKnightDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes
        
    def testBlackKnightTakeWhiteBitshopDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteBitshopsIndexes
        
    def testBlackKnightTakeWhiteRookDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteQueenIndexes
        
    def testBlackKnightTakeWhiteKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(10, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 10)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex
        
    def testBlackKnightMoveDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
    def testBlackKnightTakeWhitePawnDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whitePawnsIndexes
        
    def testBlackKnightTakeWhiteKnightDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteKnightIndexes
        
    def testBlackKnightTakeWhiteBitshopDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteBitshopsIndexes
            
    def testBlackKnightTakeWhiteRookDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteQueenIndexes
            
    def testBlackKnightTakeWhiteKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(12, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 12)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(12) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
    
    def testBlackKnightMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        
    def testBlackKnightTakeWhitePawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whitePawnsIndexes
        
    def testBlackKnightTakeWhiteKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteKnightIndexes
        
    def testBlackKnightTakeWhiteBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteBitshopsIndexes
        
    def testBlackKnightTakeWhiteRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteRooksIndexes
        
    def testBlackKnightTakeWhiteQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteQueenIndexes
    
    def testBlackKnightTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'n')
        board.setCellbyId(21, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 21)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackKnightIndexes
        assert Utils.getCellBitArrayById(21) in board.whiteKingIndex
    