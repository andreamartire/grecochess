'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

#TODO add castles
#TODO add en passant
#TODO hash positions instead of array positions

import Constants, time, Utils
from model import QuadBitBoard, Engine
from model.Move import Move, CAPTURE, QUIET

board = QuadBitBoard.QuadBitBoard()
'''start = time.clock()
for i in range(0,100000):
    Engine.getAllPseudoLegalMoves(board, Constants.BLACK)
end = time.clock()
print end - start'''

start = Utils.getCellBitArrayById(3)
end = Utils.getCellBitArrayById(57)
move = Move(start, end, Constants.QUEEN_CODE, CAPTURE) 

board.executeMove(move)

board.showBoard(2)
