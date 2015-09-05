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
        
    def testBlackPawnTakePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(30, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 30)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        assert Utils.getCellBitArrayById(30) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
    
    def testBlackPawnTakePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(28, 'P')
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 28)
         
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert len(board.whitePawnsIndexes) == 0
        assert Utils.getCellBitArrayById(28) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) not in board.whitePawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(28) in board.whitePawnsIndexes

    def testBlackPawnNoMoves(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(37, 'p')
        board.setCellbyId(29, 'P')        
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(37) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(29) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 37, 29)
        
        assert move == None
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whitePawnsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
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
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(43) in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
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
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(51) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(51) in board.blackPawnsIndexes
        