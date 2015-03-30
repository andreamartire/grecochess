'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils

#Calculate anti-diagonal distance for bitshop's moves
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
def calculateMoves():
    
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

#calculate pieces' moves only once
_bitshopMoves = calculateMoves()

def bitshopMoves():
    return _bitshopMoves