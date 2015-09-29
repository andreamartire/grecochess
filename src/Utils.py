'''
Created on Mar 28, 2015

@author: Andrea Martire
'''
from gmpy import mpz
import Constants

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

def initPiecesCode():
    _piecesCode = {}
    _piecesCode[Constants.PAWN_CODE] = "Pawn"
    _piecesCode[Constants.KNIGHT_CODE] = "Knight"
    _piecesCode[Constants.BITSHOP_CODE] = "Bitshop"
    _piecesCode[Constants.ROOK_CODE] = "Rook"
    _piecesCode[Constants.QUEEN_CODE] = "Queen"
    _piecesCode[Constants.KING_CODE] = "King"
    return _piecesCode

_piecesCode = initPiecesCode();

def getPieceByCode(pieceCode):
    return _piecesCode[pieceCode]

#usefull cells
A1 = getCellBitArrayById(0)
A8 = getCellBitArrayById(56)
C1 = getCellBitArrayById(2)
C8 = getCellBitArrayById(58)
D1 = getCellBitArrayById(3)
D8 = getCellBitArrayById(59)
E1 = getCellBitArrayById(4)
E8 = getCellBitArrayById(60)
F1 = getCellBitArrayById(5)
F8 = getCellBitArrayById(61)
G1 = getCellBitArrayById(6)
G8 = getCellBitArrayById(62)
H1 = getCellBitArrayById(7)
H8 = getCellBitArrayById(63)

PROMOTION_ROWS = mpz(0).setbit(56).setbit(57).setbit(58).setbit(59).setbit(60).setbit(61).setbit(62).setbit(63)
PROMOTION_ROWS = PROMOTION_ROWS.setbit(0).setbit(1).setbit(2).setbit(3).setbit(4).setbit(5).setbit(6).setbit(7)

EMPTY_BIT_BOARD = mpz(0)

def toggle(currPlayer):
    if(currPlayer == Constants.WHITE):
        return Constants.BLACK
    return Constants.WHITE

def cellIndexByCellName(cellName):
    base = ord('0')
    cellName = cellName.upper()
    if(cellName[0] == 'A'):
        return (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'B'):
        return 1 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'C'):
        return 2 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'D'):
        return 3 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'E'):
        return 4 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'F'):
        return 5 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'G'):
        return 6 + (ord(cellName[1])-base-1)*8
    if(cellName[0] == 'H'):
        return 7 + (ord(cellName[1])-base-1)*8
    return None
