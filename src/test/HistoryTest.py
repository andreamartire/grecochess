'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
import Utils
from model import QuadBitBoard

class HistoryTest(unittest.TestCase):
    
    def runTest(self):
        board = QuadBitBoard.QuadBitBoard()
         
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 12, 28)
         
        board.executeMove(move)
         
        assert board.moveSize == 1, 'History Error'
