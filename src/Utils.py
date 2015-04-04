'''
Created on Mar 28, 2015

@author: Andrea Martire
'''
from gmpy import mpz

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def getColumn(cellIndex):
    if(cellIndex < 0 or cellIndex > 63):
        return 
    return cellIndex % 8 + 1

@memoize
def getRow(cellIndex):
    if(cellIndex < 0 or cellIndex > 63):
        return 
    return cellIndex / 8 + 1

#precalculate ordered indexes cells for gui
def calculateCellIndexesForGui():
    _cellIndexes = range(56,64)
    _cellIndexes += range(48,56)
    _cellIndexes += range(40,48)
    _cellIndexes += range(32,40)
    _cellIndexes += range(24,32)
    _cellIndexes += range(16,24)
    _cellIndexes += range(8,16)
    _cellIndexes += range(0,8)
    return _cellIndexes

_cellIndexes = calculateCellIndexesForGui()

def getCellIndexesForGui():
    return _cellIndexes

def showCellIndexes():
    #get ordered cells indexes for gui
    cells = getCellIndexesForGui()
    
    output = ""
    for i in cells:
        if(i % 8 == 0):
            output = output + "\n"
        if(i < 10):
            output += " "
        output += `i` + " "
    print output
    return

#create bit array with an element for each board's cell
def initCellBitArray():
    _cells = {}
    for i in range(0,64):
        _cells[i] = mpz(0).setbit(i)
    return _cells

_cells = initCellBitArray();

def getCellBitArrayById(cellId):
    return _cells[cellId]

#create bit array with an element for each board's cell
def initCellPositions():
    _positions = {}
    for i in range(0,64):
        _positions[mpz(0).setbit(i)] = i
    return _positions

_positions = initCellPositions();

def getPositionByCellBitArray(cellBitBoard):
    return _positions[cellBitBoard]

#create a single bit array with all moves
def movesToBitArray(moves):
    bitBoard = mpz(0)
    for move in moves:
        bitBoard  = bitBoard | _cells[move]
    return bitBoard

def showBitArray(bitArray):
    #get ordered cells indexes for gui
    cells = getCellIndexesForGui()
    
    output = ""
    for i in cells:
        if(i % 8 == 0):
            output = output + "\n"
        if(bitArray.getbit(i) == 1):
            output += "X"
        else:
            output += "-"
    print output
    return 
