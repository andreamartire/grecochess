'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

_kingMoves = {}
    
#Precalculate king's pseudolegal moves for each cell
def calculateMoves():
        
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _kingMoves[startCellBitBoard] = []
        
        # -->
        if(col < 8):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex + 1)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        # <--
        if(col > 1):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex - 1)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #  A
        #  i
        if(row < 8):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex + 8)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #  I
        #  V
        if(row > 1):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex - 8)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #  \
        #   V
        if(row > 1 and col < 8):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex - 7)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #   /
        #  V
        if(row > 1 and col > 1):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex - 9)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #  A
        #   \
        if(row < 8 and col > 1):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex + 7)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
        #   A
        #  /
        if(row < 8 and col < 8):
            cellBitBoard = Utils.getCellBitArrayById(cellIndex + 9)
            _kingMoves[startCellBitBoard].append(cellBitBoard)
          
    return _kingMoves

#calculate pieces' moves only once
_kingMoves = calculateMoves()

def getMovesArray(cellId):
    return _kingMoves[cellId]