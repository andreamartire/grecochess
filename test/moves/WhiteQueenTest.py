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
    
    def testWhiteQueenMoveRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackPawnsIndexes
            
    def testWhiteQueenTakeBlackKnightRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKnightIndexes
            
    def testWhiteQueenTakeBlackBitshopRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackBitshopsIndexes
    
    def testWhiteQueenTakeBlackRookRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackRooksIndexes
    
    def testWhiteQueenTakeBlackQueenRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackQueenIndexes
        
    def testWhiteQueenTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(36, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 36)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
    
    def testWhiteQueenMoveLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
    def testWhiteQueenTakeBlackKnightLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKnightIndexes
            
    def testWhiteQueenTakeBlackBitshopLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackBitshopsIndexes
            
    def testWhiteQueenTakeBlackRookLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackRooksIndexes
            
    def testWhiteQueenTakeBlackQueenLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackQueenIndexes
            
    def testWhiteQueenTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(18, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 18)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(18) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(18) in board.blackKingIndex
    
    def testWhiteQueenMoveRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackPawnsIndexes
        
    def testWhiteQueenTakeBlackKnightRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes
        
    def testWhiteQueenTakeBlackBitshopRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes
        
    def testWhiteQueenTakeBlackRookRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackRooksIndexes
        
    def testWhiteQueenTakeBlackQueenRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackQueenIndexes
    
    def testWhiteQueenTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(20, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 20)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
    
    def testWhiteQueenMoveLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
    
    def testWhiteQueenTakeBlackPawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
    
    def testWhiteQueenTakeBlackKnightLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKnightIndexes
    
    def testWhiteQueenTakeBlackBitshopLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes
        
    def testWhiteQueenTakeBlackRookLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackRooksIndexes
        
    def testWhiteQueenTakeBlackQueenLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackQueenIndexes
        
    def testWhiteQueenTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(34, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 34)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(34) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
    
    def testWhiteQueenMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
            
    def testWhiteQueenTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
            
    def testWhiteQueenTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
    
    def testWhiteQueenTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
    
    def testWhiteQueenTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
    def testWhiteQueenTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(28, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
    
    def testWhiteQueenMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
    def testWhiteQueenTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
            
    def testWhiteQueenTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
            
    def testWhiteQueenTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
            
    def testWhiteQueenTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
            
    def testWhiteQueenTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(26, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
    
    def testWhiteQueenMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
    def testWhiteQueenTakeBlackPawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
    def testWhiteQueenTakeBlackKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
    def testWhiteQueenTakeBlackBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
    def testWhiteQueenTakeBlackRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
    def testWhiteQueenTakeBlackQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
    
    def testWhiteQueenTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(19, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
    
    def testWhiteQueenMoveUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
    
    def testWhiteQueenTakeBlackPawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
    
    def testWhiteQueenTakeBlackKnightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
    
    def testWhiteQueenTakeBlackBitshopUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
    def testWhiteQueenTakeBlackRookUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
    def testWhiteQueenTakeBlackQueenUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
    def testWhiteQueenTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'Q')
        board.setCellbyId(35, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteQueenIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    