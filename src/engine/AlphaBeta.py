'''
Created on 14/apr/2015

@author: Andrea Martire
'''

import Constants
from model.Generator import Generator
import copy
import Utils

class AlphaBeta(object):
    
    @staticmethod
    def calculateSolution(board, currPlayer, deep):
        v = AlphaBeta.maxValue(board, currPlayer, deep, -999, 999)
        
        for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
            #print "Analize"
            #print move
            board.executeMove(move)
            #print "Executed move" + str(deep-1)
            localMax = AlphaBeta.utility(board, currPlayer)
            #print "Check " + str(localMax) + "==" + str(v)
            if(localMax == v):
                resulMove = copy.copy(move)
                board.rollbackLastMove()
                return resulMove
                #print "Choosed"
                #print moveDecision
            board.rollbackLastMove()
        
    @staticmethod
    def minValue(board, currPlayer, deep, alpha, beta):
        #print "MinValue"
        if(deep == 1):
            return AlphaBeta.utility(board, currPlayer)
        #print "Skip deep " + str(deep)
        
        value = 999
        for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
            #print move
            board.executeMove(move)
            value = min(value, AlphaBeta.maxValue(board, Utils.toggle(currPlayer), deep-1, alpha, beta))
            #print "value <= alpha - " + str(value) + " <= " + str(alpha)
            if(value <= alpha):
                board.rollbackLastMove()
                return value
            #print "beta < alpha - " + str(beta) + " < " + str(alpha)
            if(value < beta):
                #print "change beta"
                beta = value
            #print "beta = " + str(value)
            #print "BEFORE ROLLBACK"        
            #board.showBoard(4)
            board.rollbackLastMove()
            #print "AFTER ROLLBACK"        
            #board.showBoard(4)
            #print "."
        #board.showBoard(3)
        return value 
    
    @staticmethod
    def maxValue(board, currPlayer, deep, alpha, beta):
        #print "MaxValue"
        if(deep == 1):
            return AlphaBeta.utility(board, currPlayer)
        #print "Skip deep " + str(deep)
        
        value = -999
        for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
            #print move
            board.executeMove(move)
            value = max(value, AlphaBeta.minValue(board, Utils.toggle(currPlayer), deep-1, alpha, beta))
            #print "value >= alpha - " + str(value) + " >= " + str(alpha)
            if(value >= beta):
                board.rollbackLastMove()
                return value
            #print "value > alpha - " + str(value) + " > " + str(alpha)
            if(value > alpha):
                #print "change value"
                alpha = value
            #print "value = " + str(value)
            #print "BEFORE ROLLBACK"        
            #board.showBoard(4)
            board.rollbackLastMove()
            #print "AFTER ROLLBACK"        
            #board.showBoard(4)
            #print "."
        #board.showBoard(3)
        return value
    
    @staticmethod
    def utility(board, currPlayer):    
        if(currPlayer == Constants.WHITE):
            total = len(board.whitePawnsIndexes) * 1 + len(board.whiteKnightIndexes) * 3 
            + len(board.whiteBitshopsIndexes) * 3.15 + len(board.whiteRooksIndexes) * 5
            + len(board.whiteQueenIndexes) * 9 + len(board.whiteKingIndex) * 200
        else:
            total = len(board.blackPawnsIndexes) * 1 + len(board.blackKnightIndexes) * 3
            + len(board.blackBitshopsIndexes) * 3.15 + len(board.blackRooksIndexes) * 5
            + len(board.blackQueenIndexes) * 9 + len(board.blackKingIndex) * 200
        return total
