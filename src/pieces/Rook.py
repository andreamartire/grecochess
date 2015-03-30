'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

#Precalculate rook's pseudolegal moves for each cell
def calculateMoves():
    
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
_rookMoves = calculateMoves()

def rookMoves():
    return _rookMoves
