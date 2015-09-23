'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class AlphaBetaTest(unittest.TestCase):
    
    # (Pawn,14,30,0b1)
    # (Pawn,55,39,0b1)
    # (Pawn,11,27,0b1)
    # (Pawn,39,31,0b0)
    def testPosition1(self):
        
        board = QuadBitBoard.QuadBitBoard()
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 14, 30)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 55, 39)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 2
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(39) in board.blackPawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 11, 27)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 3
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(39) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 39, 31)
        
        board.executeMove(move)
        board.checkConsistence()
        
        assert board.moveSize == 4
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        assert Utils.getCellBitArrayById(30) in board.whitePawnsIndexes
        assert Utils.getCellBitArrayById(31) in board.blackPawnsIndexes
        assert Utils.getCellBitArrayById(27) in board.whitePawnsIndexes
    
    # ->(Pawn,10,26,0b1)
    #   ->(Pawn,53,37,0b1)
    #     ->(Pawn,15,31,0b1)
    #       ->(Pawn,54,38,0b1)
    #         ->(Pawn,31,38,0b100,Pawn)
    #         <-(Pawn,31,38,0b100,Pawn)
    def testPosition2(self):
        board = QuadBitBoard.QuadBitBoard()
         
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 32
        assert len(board.whitePawnsIndexes) == 8
        assert len(board.blackPawnsIndexes) == 8
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 10, 26)
        
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 53, 37)
        
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 15, 31)
        
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 54, 38)
        
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 31, 38)
                
        board.executeMove(move)
        board.checkConsistence()
        
        board.rollbackLastMove()
        board.checkConsistence()
        
        board.checkConsistence()
        
        return
