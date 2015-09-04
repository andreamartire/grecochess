'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class BlackKingCapturedTest(unittest.TestCase):
    
    def testBlackPawnTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(19) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackPawnTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(17) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes        
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
    
    def testBlackKnightTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(30, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(30) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(14, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 14)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(14) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(14) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(14) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(14) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(37, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 37)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(37) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(37) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(35, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(35) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(26, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(26) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(10, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 10)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(10) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(10) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(3, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 3)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(3) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(3) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(3) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(3) in board.whiteKingIndex 
    
    def testBlackKnightTakeWhiteKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'n')
        board.setCellbyId(5, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 5)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes       
        assert Utils.getCellBitArrayById(5) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(5) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(5) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKnightIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackKnightIndexes        
        assert Utils.getCellBitArrayById(5) in board.whiteKingIndex 
    
    def testBlackBitshopTakeWhiteKingDownLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'b')
        board.setCellbyId(2, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 2)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
    
    def testBlackBitshopTakeWhiteKingDownRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'b')
        board.setCellbyId(6, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 6)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(6) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(6) in board.whiteKingIndex
    
    def testBlackBitshopTakeWhiteKingUpRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'b')
        board.setCellbyId(38, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 38)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(38) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(38) in board.whiteKingIndex
    
    def testBlackBitshopTakeWhiteKingUpLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(20, 'b')
        board.setCellbyId(34, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 20, 34)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(34) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackBitshopsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(20) in board.blackBitshopsIndexes       
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex
    
    def testBlackRookTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'r')
        board.setCellbyId(12, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 12)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(12) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(12) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
    
    def testBlackRookTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'r')
        board.setCellbyId(30, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(30) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex
    
    def testBlackRookTakeWhiteKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'r')
        board.setCellbyId(44, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 44)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(44) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(44) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
    
    def testBlackRookTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'r')
        board.setCellbyId(26, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(26) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackRooksIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes       
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
    def testBlackQueenTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(30, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 30)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(30) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(30) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(30) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(46, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 46)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(46) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0     
        assert Utils.getCellBitArrayById(46) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(46) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(46) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(44, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 44)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(44) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(44) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(44) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(42, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 42)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(42) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(42) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(42) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(42) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(26, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 26)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(26) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(10, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 10)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(10) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(10) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(10) in board.whiteKingIndex
    
    def testBlackQueenTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(12, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 12)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(12) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(12) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(12) in board.whiteKingIndex
        
    def testBlackQueenTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'q')
        board.setCellbyId(14, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 14)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(14) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(14) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(14) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackQueenIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes       
        assert Utils.getCellBitArrayById(14) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(29, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 29)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(29) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(29) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(29) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(29) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(37, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 37)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(37) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(37) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(37) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(36, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 36)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(36) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(36) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(36) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(35, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(35) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(27, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 27)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(27) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(27) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex
        
    def testBlackKingTakeWhiteKingLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(19, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 19)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(19) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(20, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 20)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(20) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(20) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(20) in board.whiteKingIndex
    
    def testBlackKingTakeWhiteKingRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'k')
        board.setCellbyId(21, 'K')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 21)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(21) in board.whiteKingIndex
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(21) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(21) not in board.whiteKingIndex   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackKingIndex) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex       
        assert Utils.getCellBitArrayById(21) in board.whiteKingIndex