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
            #   A
            #  /
            if(row < 8 and col < 8):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [9]
            #  A
            #  i
            if(row < 8):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [8]
            #  A
            #   \
            if(row < 8 and col > 1):
                whitePawnMoves[cellIndex] = whitePawnMoves[cellIndex] + [7]
        
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
            #   /
            #  V
            if(row > 1 and col > 1):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-9]
            #  I
            #  V
            if(row > 1):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-8]
            #  \
            #   V
            if(row > 1 and col < 8):
                blackPawnMoves[cellIndex] = blackPawnMoves[cellIndex] + [-7]
        
    return blackPawnMoves

#Calculate antidiagonal distance for bitshop moves
def antidiagonalDistance(col, row):
    if(row == 1 or col == 8):
        return 0
    elif(row == 2 or col == 7):
        return 1
    elif(row == 3 or col == 6):
        return 2
    elif(row == 4 or col == 5):
        return 3
    elif(row == 5 or col == 4):
        return 4
    elif(row == 6 or col == 3):
        return 5
    elif(row == 7 or col == 2):
        return 6
    else:
        return 7

#Precalculate bitshop pseudolegal moves for each cell
def calculateBitshopMoves():
    
    bitshopMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        bitshopMoves[cellIndex] = []
        
        #   A
        #  /
        for i in range(1,8-max(row,col)+1):
            bitshopMoves[cellIndex] = bitshopMoves[cellIndex] + [9*i]
        #  A
        #   \
        for i in range(1,antidiagonalDistance(row,col)+1):
            bitshopMoves[cellIndex] = bitshopMoves[cellIndex] + [7*i]
        #   /
        #  V
        for i in range(1,min(row,col)):
            bitshopMoves[cellIndex] = bitshopMoves[cellIndex] + [-9*i]
        #  \
        #   V
        for i in range(1,antidiagonalDistance(col,row)+1):
            bitshopMoves[cellIndex] = bitshopMoves[cellIndex] + [-7*i]
        
    return bitshopMoves

#Precalculate rook's pseudolegal moves for each cell
def calculateRookMoves():
    
    rookMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        rookMoves[cellIndex] = []
        
        #   
        #  -->
        for i in range(1,8-col+1):
            rookMoves[cellIndex] = rookMoves[cellIndex] + [1*i]
        #   A
        #   I
        for i in range(1,8-row+1):
            rookMoves[cellIndex] = rookMoves[cellIndex] + [8*i]
        #  
        #  <--
        for i in range(1,col):
            rookMoves[cellIndex] = rookMoves[cellIndex] + [-1*i]
        #   I
        #   V
        for i in range(1,row):
            rookMoves[cellIndex] = rookMoves[cellIndex] + [-8*i]
        
    return rookMoves

#calculate pieces' moves only once
_kingMoves = calculateKingMoves()
_knightMoves = calculateKnightMoves()
_whitePawnMoves = calculateWhitePawnMoves()
_blackPawnMoves = calculateBlackPawnMoves()
_bitshopMoves = calculateBitshopMoves()
_rookMoves = calculateRookMoves()

def kingMoves():
    return _kingMoves

def knightMoves():
    return _knightMoves

def whitePawnMoves():
    return _whitePawnMoves

def blackPawnMoves():
    return _blackPawnMoves

def bitshopMoves():
    return _bitshopMoves

def rookMoves():
    return _rookMoves
