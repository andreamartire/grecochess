'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

def getColumn(cellIndex):
    if(cellIndex < 0 or cellIndex > 63):
        return 
    return cellIndex % 8 + 1

def getRow(cellIndex):
    if(cellIndex < 0 or cellIndex > 63):
        return 
    return cellIndex / 8 + 1
