'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard

class WhitePawnTest(unittest.TestCase):
    
    def testWhitePawnTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
    
    def testWhitePawnTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
    
    def testWhitePawnTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'n')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
    
    def testWhitePawnTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'n')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
    
    def testWhitePawnTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'b')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
    
    def testWhitePawnTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'b')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
    
    def testWhitePawnTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'r')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
    
    def testWhitePawnTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'r')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1

    def testWhitePawnTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'q')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
    
    def testWhitePawnTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'q')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        
    def testWhitePawnTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
    
    def testWhitePawnTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        
    def testWhitePawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(34, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 34)
        
        assert move == None
        
    def testWhitePawnSinglePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 19)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
    
    def testWhitePawnDoublePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 27)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1