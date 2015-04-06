'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO hash positions instead of array positions

import Constants
import time
from model import QuadBitBoard, Engine
import Utils

board = QuadBitBoard.QuadBitBoard()
'''start = time.clock()
for i in range(0,100000):
    board.getAllPseudoLegalMoves(board, Constants.BLACK)
end = time.clock()
print end - start'''

bbFrom = Utils.getCellBitArrayById(0)
bbTo = Utils.getCellBitArrayById(27)

board.moveQuiet(bbFrom, bbTo)

Engine.getAllPseudoLegalMoves(board, Constants.WHITE)

board.showBoard(0)
