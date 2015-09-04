'''
Created on Mar 28, 2015

@author: Andrea Martire
'''
import unittest
from model import QuadBitBoard
from model.Generator import Generator
import Constants
import Utils

class BitshopTest(unittest.TestCase):
     
    def testWhiteBitshopTaskPawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
         
        board.setCellbyId(26, 'B')
        board.setCellbyId(33, 'p')
         
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.getNumOfPieces() == 1
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(33) not in board.blackPawnsIndexes
         
        board.rollbackLastMove()
         
        assert board.getNumOfPieces() == 2
        assert len(board.whiteBitshopsIndexes) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        