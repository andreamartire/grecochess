'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard

class BlackPawnTest(unittest.TestCase):
        
    def testBlackPawnTakePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(30, 'P')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 30)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
    
    def testBlackPawnTakePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(28, 'P')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 28)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1

    def testBlackPawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(29, 'P')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 29)
        
        assert move == None
        
    def testBlackPawnSinglePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 43)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
    
    def testBlackPawnDoublePush(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(51, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        