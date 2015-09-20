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
        board.showBoard(3)
         
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 12, 28)
         
        board.executeMove(move)
         
        assert board.moveSize == 1, 'History Error'
    
    def testAlphaBeta(self):
        board = QuadBitBoard.QuadBitBoard()
        board.showBoard(3)
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 15, 31)
        board.executeMove(move)
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 49, 33)
        board.executeMove(move)
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 10, 26)
        board.executeMove(move)
        
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 55, 39)
        board.executeMove(move)
         
        assert board.getNumOfPieces() == 32
