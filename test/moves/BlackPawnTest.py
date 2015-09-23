'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class BlackPawnTest(unittest.TestCase):
        
    def testBlackPawnTakeWhitePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(30, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 30)
         
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        assert Utils.getCellBitArrayById(30) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
    
    def testBlackPawnTakeWhitePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(28, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 28)
         
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
    
    def testBlackPawnTakeWhiteKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 0
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) not in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKnightIndexes
    
    def testBlackPawnTakeWhiteKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'N')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 0
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) not in board.whiteKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKnightIndexes
    
    def testBlackPawnTakeWhiteBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) not in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteBitshopsIndexes
    
    def testBlackPawnTakeWhiteBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'B')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 0
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) not in board.whiteBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteBitshopsIndexes
    
    def testBlackPawnTakeWhiteRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 0
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) not in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
    
    def testBlackPawnTakeWhiteRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 0
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) not in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteRooksIndexes

    def testBlackPawnTakeWhiteQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 0
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) not in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteQueenIndexes
    
    def testBlackPawnTakeWhiteQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'Q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 0
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) not in board.whiteQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteQueenIndexes
        
    def testBlackPawnTakeWhiteKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(19, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 19)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) not in board.whiteKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex
    
    def testBlackPawnTakeWhiteKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'p')
        board.setCellbyId(17, 'K')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 26, 17)
        
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 0
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) not in board.whiteKingIndex
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex
        
    def testBlackPawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(29, 'P')        
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(29) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 29)
        
        assert move == None
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(29) in board.whitePawnsIndexes
        
    def testBlackPawnSinglePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 43)
         
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(43) in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
    
    def testBlackPawnDoublePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 35)
         
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
    
    def testBlackEnPassantLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'p')
        board.setCellbyId(11, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 27)
           
        board.executeMove(move)
        board.checkConsistence()        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 19)
           
        board.executeMove(move)
        board.checkConsistence()
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 0
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(27) not in board.whitePawnsIndexes
         
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(11) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
           
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(11) in board.whitePawnsIndexes
    
    def testBlackEnPassantRight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(28, 'p')
        board.setCellbyId(13, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(13) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 13, 29)
           
        board.executeMove(move)
        board.checkConsistence()        
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1   
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(13) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(29) in board.whitePawnsIndexes
           
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 28, 21)
           
        board.executeMove(move)
        board.checkConsistence()
                
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 1
        assert len(board.whitePawnsIndexes) == 0
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(21) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(13) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(29) not in board.whitePawnsIndexes
         
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1  
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(13) not in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(29) in board.whitePawnsIndexes
           
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(13) in board.whitePawnsIndexes
    
    def testBlackPromotionToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 3, Constants.MOVE_KNIGHT_PROMOTION)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(3) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
    
    def testBlackPromotionToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 3, Constants.MOVE_BITSHOP_PROMOTION)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(3) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
    
    def testBlackPromotionToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 3, Constants.MOVE_ROOK_PROMOTION)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(3) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
    
    def testBlackPromotionToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(11, 'p')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 3, Constants.MOVE_QUEEN_PROMOTION)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(3) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
      
    def testBlackPromotionCaptureQueenLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingLeftToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingRightToKnight(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_KNIGHT_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackKnightIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingLeftToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingRightToBitshop(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_BITSHOP_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackBitshopsIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingLeftToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingRightToRook(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_ROOK_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackRooksIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingLeftToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(2, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 2, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(2) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(2) in board.whiteKingIndex
    
    def testBlackPromotionCaptureQueenRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'Q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteQueenIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteQueenIndexes
      
    def testBlackPromotionCaptureRookRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'R')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteRooksIndexes
      
    def testBlackPromotionCaptureBitshopRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'B')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteBitshopsIndexes
      
    def testBlackPromotionCaptureKnightRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'N')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKnightIndexes) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKnightIndexes
          
    def testBlackPromotionCaptureKingRightToQueen(self):            
        board = QuadBitBoard.QuadBitBoard()
        board.clean()

        board.setCellbyId(11, 'p')
        board.setCellbyId(4, 'K')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex
        
        move = Generator.getPromotionMoveByIndexes(board, Constants.BLACK, 11, 4, Constants.MOVE_QUEEN_PROMO_CAPTURE)
        
        board.executeMove(move)
        board.checkConsistence()

        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(4) in board.blackQueenIndexes
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whiteKingIndex) == 1
        assert Utils.getCellBitArrayById(11) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(4) in board.whiteKingIndex