'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
import Utils
from model import QuadBitBoard
from engine.AlphaBeta import AlphaBeta

class GenericTest(unittest.TestCase):
    
    def testHistorySize(self):
        board = QuadBitBoard.QuadBitBoard()
         
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 12, 28)
         
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.moveSize == 1, 'History Error'
    
    def testAlphaBeta(self):
        board = QuadBitBoard.QuadBitBoard()
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 15, 31)
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 49, 33)
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 10, 26)
        board.executeMove(move)
        board.checkConsistence()
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 55, 39)
        board.executeMove(move)
        board.checkConsistence()
         
        assert board.getNumOfPieces() == 32

    def testCellIndexByName(self):
        board = QuadBitBoard.QuadBitBoard()
        board.showBoard(2)
        
        assert Utils.cellIndexByCellName("A1") == 0
        assert Utils.cellIndexByCellName("D4") == 27
        assert Utils.cellIndexByCellName("H8") == 63
        assert Utils.cellIndexByCellName("B2") == 9
        assert Utils.cellIndexByCellName("F3") == 21
        assert Utils.cellIndexByCellName("G6") == 46
        assert Utils.cellIndexByCellName("C7") == 50