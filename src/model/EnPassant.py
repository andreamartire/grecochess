'''
Created on 14/apr/2015

@author: Andrea Martire
'''
from gmpy import mpz
import Utils

noDoublePushColumn = mpz(0)
doublePushColumnA = mpz(0).setbit(0)
doublePushColumnB = mpz(0).setbit(1)
doublePushColumnC = mpz(0).setbit(2)
doublePushColumnD = mpz(0).setbit(3)
doublePushColumnE = mpz(0).setbit(4)
doublePushColumnF = mpz(0).setbit(5)
doublePushColumnG = mpz(0).setbit(6)
doublePushColumnH = mpz(0).setbit(7)

columnByStartPosition = {}
columnByStartPosition[Utils.getCellBitArrayById(8)] = doublePushColumnA
columnByStartPosition[Utils.getCellBitArrayById(48)] = doublePushColumnA
columnByStartPosition[Utils.getCellBitArrayById(9)] = doublePushColumnB
columnByStartPosition[Utils.getCellBitArrayById(49)] = doublePushColumnB
columnByStartPosition[Utils.getCellBitArrayById(10)] = doublePushColumnC
columnByStartPosition[Utils.getCellBitArrayById(50)] = doublePushColumnC
columnByStartPosition[Utils.getCellBitArrayById(11)] = doublePushColumnD
columnByStartPosition[Utils.getCellBitArrayById(51)] = doublePushColumnD
columnByStartPosition[Utils.getCellBitArrayById(12)] = doublePushColumnE
columnByStartPosition[Utils.getCellBitArrayById(52)] = doublePushColumnE
columnByStartPosition[Utils.getCellBitArrayById(13)] = doublePushColumnF
columnByStartPosition[Utils.getCellBitArrayById(53)] = doublePushColumnF
columnByStartPosition[Utils.getCellBitArrayById(14)] = doublePushColumnG
columnByStartPosition[Utils.getCellBitArrayById(54)] = doublePushColumnG
columnByStartPosition[Utils.getCellBitArrayById(15)] = doublePushColumnH
columnByStartPosition[Utils.getCellBitArrayById(55)] = doublePushColumnH

#white
whiteEnPassantRow = mpz(0).setbit(32).setbit(33).setbit(34).setbit(35).setbit(36).setbit(37).setbit(38).setbit(39)

#black
blackEnPassantRow = mpz(0).setbit(24).setbit(25).setbit(26).setbit(27).setbit(28).setbit(29).setbit(30).setbit(31)

leftEnPassantBlock = {}
leftEnPassantBlock[Utils.getCellBitArrayById(32)] = mpz(0)
leftEnPassantBlock[Utils.getCellBitArrayById(33)] = mpz(0).setbit(40).setbit(32)
leftEnPassantBlock[Utils.getCellBitArrayById(34)] = mpz(0).setbit(41).setbit(33)
leftEnPassantBlock[Utils.getCellBitArrayById(35)] = mpz(0).setbit(42).setbit(34)
leftEnPassantBlock[Utils.getCellBitArrayById(36)] = mpz(0).setbit(43).setbit(35)
leftEnPassantBlock[Utils.getCellBitArrayById(37)] = mpz(0).setbit(44).setbit(36)
leftEnPassantBlock[Utils.getCellBitArrayById(38)] = mpz(0).setbit(45).setbit(37)
leftEnPassantBlock[Utils.getCellBitArrayById(39)] = mpz(0).setbit(46).setbit(38)

leftEnPassantBlock[Utils.getCellBitArrayById(24)] = mpz(0)
leftEnPassantBlock[Utils.getCellBitArrayById(25)] = mpz(0).setbit(16).setbit(24)
leftEnPassantBlock[Utils.getCellBitArrayById(26)] = mpz(0).setbit(17).setbit(25)
leftEnPassantBlock[Utils.getCellBitArrayById(27)] = mpz(0).setbit(18).setbit(26)
leftEnPassantBlock[Utils.getCellBitArrayById(28)] = mpz(0).setbit(19).setbit(27)
leftEnPassantBlock[Utils.getCellBitArrayById(29)] = mpz(0).setbit(20).setbit(28)
leftEnPassantBlock[Utils.getCellBitArrayById(30)] = mpz(0).setbit(21).setbit(29)
leftEnPassantBlock[Utils.getCellBitArrayById(31)] = mpz(0).setbit(22).setbit(30)

rightEnPassantBlock = {}
rightEnPassantBlock[Utils.getCellBitArrayById(32)] = mpz(0).setbit(41).setbit(33)
rightEnPassantBlock[Utils.getCellBitArrayById(33)] = mpz(0).setbit(42).setbit(34)
rightEnPassantBlock[Utils.getCellBitArrayById(34)] = mpz(0).setbit(43).setbit(35)
rightEnPassantBlock[Utils.getCellBitArrayById(35)] = mpz(0).setbit(44).setbit(36)
rightEnPassantBlock[Utils.getCellBitArrayById(36)] = mpz(0).setbit(45).setbit(37)
rightEnPassantBlock[Utils.getCellBitArrayById(37)] = mpz(0).setbit(46).setbit(38)
rightEnPassantBlock[Utils.getCellBitArrayById(38)] = mpz(0).setbit(47).setbit(39)
rightEnPassantBlock[Utils.getCellBitArrayById(39)] = mpz(0)

rightEnPassantBlock[Utils.getCellBitArrayById(24)] = mpz(0).setbit(17).setbit(25)
rightEnPassantBlock[Utils.getCellBitArrayById(25)] = mpz(0).setbit(18).setbit(26)
rightEnPassantBlock[Utils.getCellBitArrayById(26)] = mpz(0).setbit(19).setbit(27)
rightEnPassantBlock[Utils.getCellBitArrayById(27)] = mpz(0).setbit(20).setbit(28)
rightEnPassantBlock[Utils.getCellBitArrayById(28)] = mpz(0).setbit(21).setbit(29)
rightEnPassantBlock[Utils.getCellBitArrayById(29)] = mpz(0).setbit(22).setbit(30)
rightEnPassantBlock[Utils.getCellBitArrayById(30)] = mpz(0).setbit(23).setbit(31)
rightEnPassantBlock[Utils.getCellBitArrayById(31)] = mpz(0)

def getLeftEnPassantBlock(pos):
    return leftEnPassantBlock[pos]

def getRightEnPassantBlock(pos):
    return rightEnPassantBlock[pos]

capturingCellByEndPosition = {}
capturingCellByEndPosition[Utils.getCellBitArrayById(16)] = Utils.getCellBitArrayById(24)
capturingCellByEndPosition[Utils.getCellBitArrayById(17)] = Utils.getCellBitArrayById(25)
capturingCellByEndPosition[Utils.getCellBitArrayById(18)] = Utils.getCellBitArrayById(26)
capturingCellByEndPosition[Utils.getCellBitArrayById(19)] = Utils.getCellBitArrayById(27)
capturingCellByEndPosition[Utils.getCellBitArrayById(20)] = Utils.getCellBitArrayById(28)
capturingCellByEndPosition[Utils.getCellBitArrayById(21)] = Utils.getCellBitArrayById(29)
capturingCellByEndPosition[Utils.getCellBitArrayById(22)] = Utils.getCellBitArrayById(30)
capturingCellByEndPosition[Utils.getCellBitArrayById(23)] = Utils.getCellBitArrayById(31)
capturingCellByEndPosition[Utils.getCellBitArrayById(40)] = Utils.getCellBitArrayById(32)
capturingCellByEndPosition[Utils.getCellBitArrayById(41)] = Utils.getCellBitArrayById(33)
capturingCellByEndPosition[Utils.getCellBitArrayById(42)] = Utils.getCellBitArrayById(34)
capturingCellByEndPosition[Utils.getCellBitArrayById(43)] = Utils.getCellBitArrayById(35)
capturingCellByEndPosition[Utils.getCellBitArrayById(44)] = Utils.getCellBitArrayById(36)
capturingCellByEndPosition[Utils.getCellBitArrayById(45)] = Utils.getCellBitArrayById(37)
capturingCellByEndPosition[Utils.getCellBitArrayById(46)] = Utils.getCellBitArrayById(38)
capturingCellByEndPosition[Utils.getCellBitArrayById(47)] = Utils.getCellBitArrayById(39)

def getCapturingCellByEndPosition(pos):
    return capturingCellByEndPosition[pos]