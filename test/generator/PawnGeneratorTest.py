'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

from model.Generator import Generator
import Constants
import unittest
from model import QuadBitBoard
import Utils

class PawnGeneratorTest(unittest.TestCase):
    
    def testWhitePawnNoMoves(self):
        
        for i in range(0, 8):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'P')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.whitePawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.whitePawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)
            assert len(moves) == 0
                
    def testWhitePawn(self):
        
        for i in range(8,48):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'P')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.whitePawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.whitePawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)
            
            for move in moves:
                board.executeMove(move)
                board.checkConsistence()
                 
                board.showBoard(4)
                assert board.moveSize == 1
                assert board.getNumOfPieces() == 1
                assert len(board.whitePawnsIndexes) == 1
                assert move.end in board.whitePawnsIndexes
                
                board.rollbackLastMove()
                board.checkConsistence()
                
                assert board.moveSize == 0
                assert board.getNumOfPieces() == 1
                assert len(board.whitePawnsIndexes) == 1
                assert Utils.getCellBitArrayById(i) in board.whitePawnsIndexes
            
    def testWhitePawnPromotion(self):
        
        for i in range(48, 64):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'P')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.whitePawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.whitePawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.WHITE, True)
            
            for move in moves:
                board.executeMove(move)
                board.checkConsistence()
                
                assert board.moveSize == 1
                assert board.getNumOfPieces() == 1
                assert len(board.whiteQueenIndexes) + len(board.whiteRooksIndexes) + len(board.whiteBitshopsIndexes) + len(board.whiteKnightIndexes) == 1
                assert move.end in board.whiteQueenIndexes or move.end in board.whiteRooksIndexes or move.end in board.whiteBitshopsIndexes or move.end in board.whiteKnightIndexes
                
                board.rollbackLastMove()
                board.checkConsistence()
                
                assert board.moveSize == 0
                assert board.getNumOfPieces() == 1
                assert len(board.whitePawnsIndexes) == 1
                assert Utils.getCellBitArrayById(i) in board.whitePawnsIndexes
        
    def testBlackPawnNoMoves(self):
        
        for i in range(56, 64):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'p')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.blackPawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.blackPawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)
            assert len(moves) == 0
                
    def testBlackPawn(self):
        
        for i in range(23, 56):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'p')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.blackPawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.blackPawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)
            
            for move in moves:
                board.executeMove(move)
                board.checkConsistence()
                 
                board.showBoard(4)
                assert board.moveSize == 1
                assert board.getNumOfPieces() == 1
                assert len(board.blackPawnsIndexes) == 1
                assert move.end in board.blackPawnsIndexes
                
                board.rollbackLastMove()
                board.checkConsistence()
                
                assert board.moveSize == 0
                assert board.getNumOfPieces() == 1
                assert len(board.blackPawnsIndexes) == 1
                assert Utils.getCellBitArrayById(i) in board.blackPawnsIndexes
            
    def testBlackPawnPromotion(self):
        
        for i in range(8, 16):
            board = QuadBitBoard.QuadBitBoard()
            board.clean()
            
            board.setCellbyId(i, 'p')
             
            assert board.moveSize == 0
            assert board.getNumOfPieces() == 1
            assert len(board.blackPawnsIndexes) == 1
            assert Utils.getCellBitArrayById(i) in board.blackPawnsIndexes
            
            moves = Generator.getAllPseudoLegalMoves(board, Constants.BLACK, True)
            
            for move in moves:
                board.executeMove(move)
                board.checkConsistence()
                
                assert board.moveSize == 1
                assert board.getNumOfPieces() == 1
                assert len(board.blackQueenIndexes) + len(board.blackRooksIndexes) + len(board.blackBitshopsIndexes) + len(board.blackKnightIndexes) == 1
                assert move.end in board.blackQueenIndexes or move.end in board.blackRooksIndexes or move.end in board.blackBitshopsIndexes or move.end in board.blackKnightIndexes
                
                board.rollbackLastMove()
                board.showBoard(4)
                board.checkConsistence()
                
                assert board.moveSize == 0
                assert board.getNumOfPieces() == 1
                assert len(board.blackPawnsIndexes) == 1
                assert Utils.getCellBitArrayById(i) in board.blackPawnsIndexes
                        