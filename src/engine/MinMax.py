'''
Created on 14/apr/2015

@author: Andrea Martire
'''

import Constants
from model.Generator import Generator
import copy

def calculateSolution(board, currPlayer, deep):
    print "MinMaxDecision"
    v = -999
    moveDecision = 2
    for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
        #print "Analize"
        #print move
        board.executeMove(move)
        #print "Executed move" + str(deep-1)
        localMax = maxValue(board, swapPlayer(currPlayer), deep)
        #print "Check " + str(localMax) + ">" + str(v)
        if(localMax > v):
            v = localMax
            moveDecision = copy.copy(move)
            #print "Choosed"
            #print moveDecision
        board.rollbackLastMove()
    return moveDecision
        
def minValue(board, currPlayer, deep):
    #print "MinValue"
    if(deep == 1):
        return utility(board, currPlayer)
    #print "Skip deep" + str(deep)
    
    value = 999
    for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
        #print move
        board.executeMove(move)
        value = min(value, maxValue(board, swapPlayer(currPlayer), deep-1))
        #print "BEFORE ROLLBACK"        
        #board.showBoard(4)
        board.rollbackLastMove()
        #print "AFTER ROLLBACK"        
        #board.showBoard(4)
        #print "."
    return value 

def maxValue(board, currPlayer, deep):
    #print "MaxValue"
    if(deep == 1):
        return utility(board, currPlayer)
    #print "Skip deep" + str(deep)
    
    value = -999
    for move in Generator.getAllPseudoLegalMoves(board, currPlayer, True):
        #print move
        board.executeMove(move)
        value = max(value, minValue(board, swapPlayer(currPlayer), deep-1))
        #print "BEFORE ROLLBACK"        
        #board.showBoard(4)
        board.rollbackLastMove()
        #print "AFTER ROLLBACK"        
        #board.showBoard(4)
        #print "."
    return value
    
def swapPlayer(currPlayer):
    if(currPlayer == Constants.WHITE):
        return Constants.BLACK
    return Constants.WHITE

def utility(board, currPlayer):    
    if(currPlayer == Constants.WHITE):
        total = len(board.whitePawnsIndexes) * 1 + len(board.whiteKnightIndexes) * 3 
        total += len(board.whiteBitshopsIndexes) * 3.15 + len(board.whiteRooksIndexes) * 5
        total += len(board.whiteQueenIndexes) * 9 + len(board.whiteKingIndex) * 200
    else:
        total = len(board.blackPawnsIndexes) * 1 + len(board.blackKnightIndexes) * 3
        total += len(board.blackBitshopsIndexes) * 3.15 + len(board.blackRooksIndexes) * 5
        total += len(board.blackQueenIndexes) * 9 + len(board.blackKingIndex) * 200
    return total
