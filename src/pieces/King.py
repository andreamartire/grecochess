'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

#Precalculate king's pseudolegal moves for each cell
def calculateMoves():
    
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

#calculate pieces' moves only once
_kingMoves = calculateMoves()

def kingMoves():
    return _kingMoves