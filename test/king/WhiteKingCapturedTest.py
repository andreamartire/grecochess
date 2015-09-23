'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteKingCapturedTest(unittest.TestCase):
    
    def testWhitePawnTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(35) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    
    def testWhitePawnTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(33) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes        
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
    
    def testWhiteKnightTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(30, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(30) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(14, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 14)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(14) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(14) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(14) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(14) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(37, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 37)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(37) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(37) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(35, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(35) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(35) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(26, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(26) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(26) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(10, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 10)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(10) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(10) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(3, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 3)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(3) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(3) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(3) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(3) in board.blackKingIndex 
    
    def testWhiteKnightTakeBlackKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'N')
        board.setCellbyId(5, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 5)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes       
        assert Utils.getCellBitArrayById(5) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(5) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(5) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKnightIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteKnightIndexes        
        assert Utils.getCellBitArrayById(5) in board.blackKingIndex 
    
    def testWhiteBitshopTakeBlackKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'B')
        board.setCellbyId(2, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 2)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) in board.blackKingIndex
    
    def testWhiteBitshopTakeBlackKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'B')
        board.setCellbyId(6, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 6)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(6) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) in board.blackKingIndex
    
    def testWhiteBitshopTakeBlackKingUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'B')
        board.setCellbyId(38, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 38)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(38) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) in board.blackKingIndex
    
    def testWhiteBitshopTakeBlackKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'B')
        board.setCellbyId(34, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 20, 34)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(34) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.whiteBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) in board.blackKingIndex
    
    def testWhiteRookTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'R')
        board.setCellbyId(12, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 12)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(12) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(12) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
    
    def testWhiteRookTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'R')
        board.setCellbyId(30, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(30) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex
    
    def testWhiteRookTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'R')
        board.setCellbyId(44, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 44)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(44) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(44) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(44) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(44) in board.blackKingIndex
    
    def testWhiteRookTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'R')
        board.setCellbyId(26, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(26) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes       
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
    def testWhiteQueenTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(30, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(30) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(30) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(46, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 46)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(46) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0     
        assert Utils.getCellBitArrayById(46) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(46) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(46) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(44, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 44)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(44) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(44) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(44) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(44) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(42, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 42)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(42) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(42) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(42) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(42) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(26, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(26) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(26) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(10, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 10)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(10) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(10) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(10) in board.blackKingIndex
    
    def testWhiteQueenTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(12, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 12)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(12) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(12) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(12) in board.blackKingIndex
        
    def testWhiteQueenTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'Q')
        board.setCellbyId(14, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 14)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(14) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(14) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(14) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteQueenIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteQueenIndexes       
        assert Utils.getCellBitArrayById(14) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(29, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 29)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(29) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(29) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(29) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(29) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(37, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 37)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(37) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(36, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 36)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(36) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(35, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(35) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(27, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 27)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(27) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex
        
    def testWhiteKingTakeBlackKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(19, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 19)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(19) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(20, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 20)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(20) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex
    
    def testWhiteKingTakeBlackKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'K')
        board.setCellbyId(21, 'k')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 21)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(21) in board.blackKingIndex
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(21) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(21) not in board.blackKingIndex   
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteKingIndex       
        assert Utils.getCellBitArrayById(21) in board.blackKingIndex