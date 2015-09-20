'''
Created on Mar 28, 1915

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class BlackRookTest(unittest.TestCase):
    
    def testBlackRookMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
    def testBlackRookTakeWhitePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
            
    def testBlackRookTakeWhiteKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKnightIndexes
            
    def testBlackRookTakeWhiteBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteBitshopsIndexes
    
    def testBlackRookTakeWhiteRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
    
    def testBlackRookTakeWhiteQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
    def testBlackRookTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(28, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex
    
    def testBlackRookMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
    def testBlackRookTakeWhitePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        
    def testBlackRookTakeWhiteKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes
            
    def testBlackRookTakeWhiteBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
            
    def testBlackRookTakeWhiteRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
            
    def testBlackRookTakeWhiteQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
            
    def testBlackRookTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(26, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
    
    def testBlackRookMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
    def testBlackRookTakeWhitePawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        
    def testBlackRookTakeWhiteKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
    def testBlackRookTakeWhiteBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
    def testBlackRookTakeWhiteRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
    def testBlackRookTakeWhiteQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
    
    def testBlackRookTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(19, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackRookMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
    
    def testBlackRookTakeWhitePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'P')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
    
    def testBlackRookTakeWhiteKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes
    
    def testBlackRookTakeWhiteBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteBitshopsIndexes
        
    def testBlackRookTakeWhiteRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
    def testBlackRookTakeWhiteQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
    def testBlackRookTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'r')
        board.setCellbyId(35, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.blackRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
    