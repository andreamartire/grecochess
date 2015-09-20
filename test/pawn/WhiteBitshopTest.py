'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteBitshopTest(unittest.TestCase):
    
    def testWhiteBitshopMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
    def testWhiteBitshopTakeBlackPawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
            
    def testWhiteBitshopTakeBlackKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
            
    def testWhiteBitshopTakeBlackBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
    
    def testWhiteBitshopTakeBlackRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
    
    def testWhiteBitshopTakeBlackQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
    def testWhiteBitshopTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        board.showBoard(2)
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(36, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
    
    def testWhiteBitshopMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
    def testWhiteBitshopTakeBlackPawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
    def testWhiteBitshopTakeBlackKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
            
    def testWhiteBitshopTakeBlackBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
            
    def testWhiteBitshopTakeBlackRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
            
    def testWhiteBitshopTakeBlackQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
            
    def testWhiteBitshopTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(18, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
    
    def testWhiteBitshopMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
    def testWhiteBitshopTakeBlackPawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
    def testWhiteBitshopTakeBlackKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
    def testWhiteBitshopTakeBlackBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
    def testWhiteBitshopTakeBlackRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
    def testWhiteBitshopTakeBlackQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
    
    def testWhiteBitshopTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(20, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
    
    def testWhiteBitshopMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.showBoard(4)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
    
    def testWhiteBitshopTakeBlackPawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
    
    def testWhiteBitshopTakeBlackKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
    
    def testWhiteBitshopTakeBlackBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
    def testWhiteBitshopTakeBlackRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
    def testWhiteBitshopTakeBlackQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
    def testWhiteBitshopTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'B')
        board.setCellbyId(34, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
    