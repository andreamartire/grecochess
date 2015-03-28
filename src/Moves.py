'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

import Utils

#Precalculate knight's pseudolegal moves for each cell
def calculateKnightMoves():
    
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

#Precalculate king's pseudolegal moves for each cell
def calculateKingMoves():
    
    kingMoves = {}
        
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        kingMoves[cellIndex] = []
        
        # -->
        if(col < 8):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [1]
        # <--
        if(col > 1):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [-1]
        #  A
        #  i
        if(row < 8):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [8]
        #  I
        #  V
        if(row > 1):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [-8]
        #  \
        #   V
        if(row > 1 and col < 8):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [-7]
        #   /
        #  V
        if(row > 1 and col > 1):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [-9]
        #  A
        #   \
        if(row < 8 and col > 1):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [7]
        #   A
        #  /
        if(row < 8 and col < 8):
            kingMoves[cellIndex] = kingMoves[cellIndex] + [9]
          
    return kingMoves

#Precalculate white pawn's pseudolegal moves for each cell
def calculateWhitePawnMoves():
    
    whitePawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        whitePawnMoves[cellIndex] = []
        
        if(row > 1):
            #  A
            #  i
            if(row < 8):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [8]
            #  A
            #   \
            if(row < 8 and col > 1):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [7]
            #   A
            #  /
            if(row < 8 and col < 8):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [9]
        
    return whitePawnMoves

#Precalculate black pawn's pseudolegal moves for each cell
def calculateBlackPawnMoves():
    
    blackPawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        blackPawnMoves[cellIndex] = []
        
        if(row < 8):
            #  I
            #  V
            if(row > 1):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-8]
            #  \
            #   V
            if(row > 1 and col < 8):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-7]
            #   /
            #  V
            if(row > 1 and col > 1):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-9]
        
    return blackPawnMoves

#calculate pieces' moves only once
_kingMoves = calculateKingMoves()
_knightMoves = calculateKnightMoves()
_whitePawnMoves = calculateWhitePawnMoves()
_blackPawnMoves = calculateBlackPawnMoves()

def kingMoves():
    return _kingMoves

def knightMoves():
    return _knightMoves

def whitePawnMoves():
    return _whitePawnMoves

def blackPawnMoves():
    return _blackPawnMoves