'''
Created on Mar 28, 1915

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteRookTest(unittest.TestCase):
    
    def testWhiteRookMoveRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
    def testWhiteRookTakeBlackPawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
            
    def testWhiteRookTakeBlackKnightRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKnightIndexes
            
    def testWhiteRookTakeBlackBitshopRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackBitshopsIndexes
    
    def testWhiteRookTakeBlackRookRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'r')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackRooksIndexes
    
    def testWhiteRookTakeBlackQueenRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'q')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackQueenIndexes
        
    def testWhiteRookTakeBlackKingRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(28, 'k')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 28)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(28) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(28) in board.blackKingIndex
    
    def testWhiteRookMoveLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
    def testWhiteRookTakeBlackPawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackPawnsIndexes
        
    def testWhiteRookTakeBlackKnightLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKnightIndexes
            
    def testWhiteRookTakeBlackBitshopLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackBitshopsIndexes
            
    def testWhiteRookTakeBlackRookLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackRooksIndexes
            
    def testWhiteRookTakeBlackQueenLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackQueenIndexes
            
    def testWhiteRookTakeBlackKingLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(26, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 26)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(26) in board.blackKingIndex
    
    def testWhiteRookMoveDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
    def testWhiteRookTakeBlackPawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
    def testWhiteRookTakeBlackKnightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKnightIndexes
        
    def testWhiteRookTakeBlackBitshopDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackBitshopsIndexes
        
    def testWhiteRookTakeBlackRookDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackRooksIndexes
        
    def testWhiteRookTakeBlackQueenDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackQueenIndexes
    
    def testWhiteRookTakeBlackKingDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(19, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 19)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(19) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(19) in board.blackKingIndex
    
    def testWhiteRookMoveUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
    
    def testWhiteRookTakeBlackPawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'p')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
    
    def testWhiteRookTakeBlackKnightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'n')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKnightIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKnightIndexes
    
    def testWhiteRookTakeBlackBitshopUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'b')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackBitshopsIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackBitshopsIndexes
        
    def testWhiteRookTakeBlackRookUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'r')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackRooksIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackRooksIndexes
        
    def testWhiteRookTakeBlackQueenUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'q')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackQueenIndexes) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackQueenIndexes
        
    def testWhiteRookTakeBlackKingUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(27, 'R')
        board.setCellbyId(35, 'k')
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 27, 35)
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteRooksIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.whiteRooksIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteRooksIndexes) == 1
        assert len(board.blackKingIndex) == 1
        assert Utils.getCellBitArrayById(27) in board.whiteRooksIndexes
        assert Utils.getCellBitArrayById(35) in board.blackKingIndex
    