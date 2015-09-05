'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhitePawnTest(unittest.TestCase):
    
    def testWhitePawnTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
    
    def testWhitePawnTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
    
    def testWhitePawnTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
    
    def testWhitePawnTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackKnightIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKnightIndexes
    
    def testWhitePawnTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
    
    def testWhitePawnTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackBitshopsIndexes
    
    def testWhitePawnTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
    
    def testWhitePawnTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackRooksIndexes

    def testWhitePawnTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
    
    def testWhitePawnTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackQueenIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackQueenIndexes
        
    def testWhitePawnTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(35, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(35) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    
    def testWhitePawnTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(33, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 0
        assert Utils.getCellBitArrayById(33) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackKingIndex
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackKingIndex
        
    def testWhitePawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'P')
        board.setCellbyId(34, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 34)
        
        assert move == None         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
    def testWhitePawnSinglePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 19)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
    
    def testWhitePawnDoublePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 27)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
    def testWhiteEnPassantLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(36, 'P')
        board.setCellbyId(51, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 35)
           
        board.executeMove(move)        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 36, 43)
           
        board.executeMove(move)
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(43) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) not in board.blackPawnsIndexes
         
        board.rollbackLastMove()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes 
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
           
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
    
    def testWhiteEnPassantRight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(36, 'P')
        board.setCellbyId(53, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 53, 37)
           
        board.executeMove(move)        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 36, 45)
           
        board.executeMove(move)
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(45) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) not in board.blackPawnsIndexes
         
        board.rollbackLastMove()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes 
        assert Utils.getCellBitArrayById(53) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
           
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(36) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(53) in board.blackPawnsIndexes