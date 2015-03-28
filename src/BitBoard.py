from gmpy import mpz

class BitBoard(object):
    #white
    whitePieces = 0
    whitePawns = 0
    whiteKnight = 0
    whiteBitshops = 0
    whiteRooks = 0
    whiteKing = 0
    whiteQueen = 0
    
    #black
    blackPieces = 0
    blackPawns = 0
    blackKnight = 0
    blackBitshops = 0
    blackRooks = 0
    blackKing = 0
    blackQueen = 0
    
    def __init__(self):                
        #White Pieces
        self.whitePieces = mpz(0)
        for num in range(0,16):
            self.whitePieces = self.whitePieces.setbit(num)
        #print 'White Pieces=' + bin(self.whitePieces)
        
        self.whitePawns = mpz(0)
        for num in range(8,16):
            self.whitePawns = self.whitePawns.setbit(num)
        #print 'White Pawns=' + bin(self.whitePawns)
        
        self.whiteKnight = mpz(0).setbit(1).setbit(6)
        #print 'White Horses=' + bin(self.whiteKnight)
        
        self.whiteBitshops = mpz(0).setbit(2).setbit(5)
        #print 'White Bitshops=' + bin(self.whiteBitshops)
        
        self.whiteRooks = mpz(0).setbit(0).setbit(7)
        #print 'White Rooks=' + bin(self.whiteRooks)
        
        self.whiteKing = mpz(0).setbit(4)
        #print 'White King=' + bin(self.whiteKing)
        
        self.whiteQueen = mpz(0).setbit(3)
        #print 'White Queen=' + bin(self.whiteQueen)
        
        #Black Pieces
        self.blackPieces = mpz(0)
        for num in range(48,64):
            self.blackPieces = self.blackPieces.setbit(num)
        #print 'Black Pieces\t' + bin(blackPieces)
        
        self.blackPawns = mpz(0)
        for num in range(48,56):
            self.blackPawns = self.blackPawns.setbit(num)
        #print 'Black Pawns=' + bin(self.blackPawns)
        
        self.blackKnight = mpz(0).setbit(57).setbit(62)
        #print 'Black Horses\t' + bin(self.blackKnight)
        
        self.blackBitshops = mpz(0).setbit(58).setbit(61)
        #print 'Black Bitshops\t' + bin(self.blackBitshops)
        
        self.blackRooks = mpz(0).setbit(56).setbit(63)
        #print 'Black Rooks\t' + bin(self.blackRooks)
        
        self.blackKing = mpz(0).setbit(60)
        #print 'Black King\t' + bin(self.blackKing)
        
        self.blackQueen = mpz(0).setbit(59)
        #print 'Black Queen\t' + bin(self.blackQueen)

    def showBoard(self):
        #generate ordered cells for gui
        cells = range(56,64)
        cells = cells + range(48,56)
        cells = cells + range(40,48)
        cells = cells + range(32,40)
        cells = cells + range(24,32)
        cells = cells + range(16,24)
        cells = cells + range(8,16)
        cells = cells + range(0,8)
        
        output = ""
        for i in cells:
            if(i % 8 == 0):
                output = output + "\n"
            if(self.blackPieces.getbit(i) == 1):
                if(self.blackRooks.getbit(i) == 1):
                    output = output + "r"
                elif(self.blackKnight.getbit(i) == 1):
                    output = output + "n"
                elif(self.blackBitshops.getbit(i) == 1):
                    output = output + "b"
                elif(self.blackPawns.getbit(i) == 1):
                    output = output + "p"
                elif(self.blackQueen.getbit(i) == 1):
                    output = output + "q"
                elif(self.blackKing.getbit(i) == 1):
                    output = output + "k"
            elif(self.whitePieces.getbit(i) == 1):
                if(self.whiteRooks.getbit(i) == 1):
                    output = output + "R"
                elif(self.whiteKnight.getbit(i) == 1):
                    output = output + "N"
                elif(self.whiteBitshops.getbit(i) == 1):
                    output = output + "B"
                elif(self.whitePawns.getbit(i) == 1):
                    output = output + "P"
                elif(self.whiteQueen.getbit(i) == 1):
                    output = output + "Q"
                elif(self.whiteKing.getbit(i) == 1):
                    output = output + "K"
            else:
                output = output + "-"
        print output
        return 