'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

#Precalculate knight's pseudolegal moves for each cell
def calculateMoves():
    
    knightMoves = {}
        
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        knightMoves[cellIndex] = []
        
        #   I
        #   I
        # __I 
        #
        if(row > 2 and col > 1):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [-17]
        # I
        # I
        # I__
        #
        if(row > 2 and col < 8):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [-15]
        # ____
        # I
        #
        if(row > 1 and col > 2):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [-10]
        # ____
        #    I
        #
        if(row > 1 and col < 7):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [-6]
        #    
        # ___I
        #
        if(row < 8 and col < 7):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [10]
        #    
        # I___
        #
        if(row < 8 and col > 2):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [6]
        # ___
        # I 
        # I 
        # I
        if(row < 7 and col < 8):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [17]
        # ___
        #   I 
        #   I 
        #   I
        if(row < 7 and col > 1):
            knightMoves[cellIndex] = knightMoves[cellIndex] + [15]
    return knightMoves

#calculate pieces' moves only once
_knightMoves = calculateMoves()

def knightMoves():
    return _knightMoves