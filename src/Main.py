'''
Created on Mar 28, 2015

@author: Andrea Martire
'''

import Constants, time
from model import QuadBitBoard

from model.Generator import Generator
from engine.AlphaBeta import AlphaBeta

board = QuadBitBoard.QuadBitBoard()

start_time = time.time()

move = AlphaBeta.calculateSolution(board, Constants.WHITE, 8)

print "Solution: " + str(move)
print "Moves Executed: " + str(board.moveCounterExecution)
print "Cache Add Counter : " + str(Generator.cacheAddCounter)
print "Cache Reuse Counter : " + str(Generator.cacheReuseCounter)

print("--- %s seconds ---" % (time.time() - start_time))