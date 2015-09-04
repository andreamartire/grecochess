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
         
        assert board.moveSize == 1, 'History Error'
    
    def AlphaBeta(self):
        board = QuadBitBoard.QuadBitBoard()
        board.showBoard(3)
        
        AlphaBeta.calculateSolution(board, Constants.WHITE, 6)
         
        assert board.getNumOfPieces() == 32
