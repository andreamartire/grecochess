'''
Created on Mar 28, 2015

@author: Andrea Martire
'''


from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class WhiteKingCapturingPawnTest(unittest.TestCase):
    
    def testWhiteKingTakePawnRight(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(27, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 27)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(27) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0     
        assert Utils.getCellBitArrayById(27) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(27) not in board.blackPawnsIndexes   
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(27) in board.blackPawnsIndexes
        
    def testWhiteKingTakePawnRightUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(35, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 35)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(35) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(35) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(35) in board.blackPawnsIndexes
        
    def testWhiteKingTakePawnUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(34, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 34)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(34) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(34) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(34) in board.blackPawnsIndexes
    
    def testWhiteKingTakePawnLeftUp(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(33, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 33)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(33) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(33) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(33) in board.blackPawnsIndexes
    
    def testWhiteKingTakePawnLeft(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(25, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 25)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(25) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(25) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(25) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(25) in board.blackPawnsIndexes
    
    def testWhiteKingTakePawnLeftDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(17, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 17)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(17) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(17) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(17) in board.blackPawnsIndexes
        
    def testWhiteKingTakePawnDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(18, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 18)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(18) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(18) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(18) in board.blackPawnsIndexes
        
    def testWhiteKingTakePawnRightDown(self):
        board = QuadBitBoard.QuadBitBoard()
        board.clean()
        
        board.setCellbyId(26, 'K')
        board.setCellbyId(19, 'p')
        
        move = Generator.getMoveByIndexes(board, Constants.WHITE, 26, 19)
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
        board.executeMove(move)
         
        assert board.moveSize == 1
        assert board.getNumOfPieces() == 1
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 0
        assert Utils.getCellBitArrayById(19) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(19) not in board.blackPawnsIndexes
        
        board.rollbackLastMove()
        
        assert board.moveSize == 0
        assert board.getNumOfPieces() == 2
        assert len(board.whiteKingIndex) == 1
        assert len(board.blackPawnsIndexes) == 1
        assert Utils.getCellBitArrayById(26) in board.whiteKingIndex        
        assert Utils.getCellBitArrayById(19) in board.blackPawnsIndexes
        
    