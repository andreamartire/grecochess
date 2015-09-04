from model import QuadBitBoard
from model.Generator import Generator
import Constants
import Utils
import unittest

class EnPassantWhiteLeft(unittest.TestCase):
    
    def runTest(self):
        board = QuadBitBoard.QuadBitBoard()
          
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 12, 28)
           
        board.executeMove(move)        
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 28, 36)
           
        board.executeMove(move)
         
        move = Generator.getMoveByIndexes(board, Constants.BLACK, 51, 35)
         
        board.executeMove(move)
           
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 36, 43)
           
        board.executeMove(move)
  
        assert board.getNumOfPieces() == 31
        assert Utils.getCellBitArrayById(43) in board.whitePawnsIndexes