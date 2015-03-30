'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

#directions
LEFT = 0;
UP = 1;
RIGHT = 2;

#Precalculate white pawn's pseudolegal moves for each cell
def calculateWhitePawnMoves():
    
    whitePawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        whitePawnMoves[cellIndex] = {}
        whitePawnMoves[cellIndex][RIGHT] = []
        whitePawnMoves[cellIndex][UP] = []
        whitePawnMoves[cellIndex][LEFT] = []
        
        if(row > 1):
            #  A
            #   \
            if(row < 8 and col > 1):
                whitePawnMoves[cellIndex][LEFT] = whitePawnMoves[cellIndex][LEFT] + [7]
            #  A
            #  i
            if(row < 8):
                whitePawnMoves[cellIndex][UP] = whitePawnMoves[cellIndex][UP] + [8]
            #  A
            #  i
            #  i
            if(row == 2):
                whitePawnMoves[cellIndex][UP] = whitePawnMoves[cellIndex][UP] + [8*2]    
            #   A
            #  /
            if(row < 8 and col < 8):
                whitePawnMoves[cellIndex][RIGHT] = whitePawnMoves[cellIndex][RIGHT] + [9]
        
    return whitePawnMoves

#Precalculate black pawn's pseudolegal moves for each cell
def calculateBlackPawnMoves():
    
    blackPawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        blackPawnMoves[cellIndex] = {}
        blackPawnMoves[cellIndex][RIGHT] = []
        blackPawnMoves[cellIndex][UP] = []
        blackPawnMoves[cellIndex][LEFT] = []
        
        if(row < 8):
            #  \
            #   V
            if(row > 1 and col < 8):
                blackPawnMoves[cellIndex][LEFT] = blackPawnMoves[cellIndex][LEFT] + [-7]
            #  I
            #  V
            if(row > 1):
                blackPawnMoves[cellIndex][UP] = blackPawnMoves[cellIndex][UP] + [-8]
            #  l
            #  l
            #  V
            if(row == 7):
                blackPawnMoves[cellIndex][UP] = blackPawnMoves[cellIndex][UP] + [-8*2]  
            #   /
            #  V
            if(row > 1 and col > 1):
                blackPawnMoves[cellIndex][RIGHT] = blackPawnMoves[cellIndex][RIGHT] + [-9]
    
    return blackPawnMoves

#calculate pieces' moves only once
_whitePawnMoves = calculateWhitePawnMoves()
_blackPawnMoves = calculateBlackPawnMoves()

def whitePawnMoves():
    return _whitePawnMoves

def blackPawnMoves():
    return _blackPawnMoves