'''
Created on 25/apr/2015

@author: Andrea Martire
'''
import Constants

def getCapturingMove(bb, pos):
    #rooks
    if( bb.rqk & ~bb.pbq & ~bb.nbk & pos == pos):
        return Constants.MOVE_ROOK_PROMO_CAPTURE
    #knigths
    elif(~bb.rqk & ~bb.pbq &  bb.nbk & pos == pos):
        return Constants.MOVE_KNIGHT_PROMO_CAPTURE
    #bitshops
    elif( bb.pbq &  bb.nbk             & pos == pos):
        return Constants.MOVE_BITSHOP_PROMO_CAPTURE
    #queens
    elif( bb.rqk &  bb.pbq             & pos == pos):
        return Constants.MOVE_QUEEN_PROMO_CAPTURE
    #kings
    elif( bb.rqk &              bb.nbk & pos == pos):
        return Constants.MOVE_KING_PROMO_CAPTURE
    return Constants.MOVE_PAWN_PROMO_CAPTURE 