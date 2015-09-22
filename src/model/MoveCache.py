'''
Transposition Table

@author: Andrea Martire
'''
import Constants

whiteCache = {}
blackCache = {}

cleaningMap = {}
#init map
for i in range(1, 33):
    cleaningMap[i] = []

class MoveCache(object):
    
    @staticmethod
    def put(color, board, moveList):
        hashcode = board.getHash()
        if(color == Constants.WHITE):
            whiteCache[hashcode] = moveList
        else:
            blackCache[hashcode] = moveList
        
        #board.showBoard(3)
        
        #save the support information to facilitate the operation of the cache cleaning
        cleaningMap[board.getNumOfPieces()].append(hashcode)
        return 
    
    @staticmethod
    def get(color, hashcode):
        if(color == Constants.WHITE):
            return whiteCache.get(hashcode)
        return blackCache.get(hashcode)
    
    @staticmethod
    def cleanUnusefulMoves(bb):   
        print "Before. WhiteCache: " + str(len(whiteCache)) + " BlackCache: " + str(len(blackCache))    
        #remove moves relative to boards with less pieces
        for i in range(bb.getNumOfPieces()+1, 33):
            for hashCode in cleaningMap[i]:
                whiteCache.pop(hashCode, None)
                blackCache.pop(hashCode, None)
            del cleaningMap[i]
        print "After. WhiteCache: " + str(len(whiteCache)) + " BlackCache: " + str(len(blackCache))
        return
    