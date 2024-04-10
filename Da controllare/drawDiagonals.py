def drawDiagonals(pict):
    
    # @param pict: picture
    
    side = getWidth(pict)
    side2 = side / 2
   
    for i in range(0, side):
        diagonal = getPixel(pict, i, i)
        antiDiagonal = getPixel(pict, side - i - 1, i)
        setColor(diagonal, black)
        setColor(antiDiagonal, black)
        
    for j in range(0, side2):
        botDiagonalDx = getPixel(pict, side2 + j, side - j - 1)
        botDiagonalSx = getPixel(pict, side2 - j, side - j - 1)
        setColor(botDiagonalDx, black)
        setColor(botDiagonalSx, black)
    
    repaint(pict)
        
myPict = makeEmptyPicture(500, 500)
drawDiagonals(myPict)
