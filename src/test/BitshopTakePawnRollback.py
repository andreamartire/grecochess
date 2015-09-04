'''
Created on Mar 28, 2015

@author: Andrea Martire
'''
import unittest
from model import QuadBitBoard
from model.Generator import Generator
import Constants
import Utils

class BitshopTakePawnRollback(unittest.TestCase):
     
    def runTest(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
         
        board.setCellbyId(5, 'B')
        board.setCellbyId(33, 'p')
         
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 5, 33)
         
        board.executeMove(move)
         
        assert board.getNumOfPieces() == 1
        assert Utils.getCellBitArrayById(33) in board.whiteBitshopsIndexes
         
        board.rollbackLastMove()
         
        assert board.getNumOfPieces() == 2
        assert Utils.getCellBitArrayById(5) in board.whiteBitshopsIndexes
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes