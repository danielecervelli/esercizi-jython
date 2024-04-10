def drawLadder(pict, base, height):

    # @param pict: picture
    # @param base: int
    # @param height: int

    y = 0
    for x in range(0, getWidth(pict), base):
        horizontalLine(pict, base, x, min(y + height, getHeight(pict) - 1))
        y += height
    
    x = 0
    for y in range(height, getHeight(pict), height):
        VerticalLine(pict, height, min(x + base, getWidth(pict) - 1), y)
        x += base
        
    repaint(pict)


def horizontalLine(pict, lenght, x, y):

    # @param pict: picture
    # @param lenght: int
    # @param x: int
    # @param y: int
    
    for i in range(0, lenght):
        px = getPixel(pict, min(x + i, getWidth(pict) - 1), y)
        setColor(px, black)


def VerticalLine(pict, height, x, y):

    # @param pict: picture
    # @param height: int
    # @param x: int
    # @param y: int
    
    for j in range(0, height):
        px = getPixel(pict, x, min(y + j, getHeight(pict) - 1))
        setColor(px, black)
        
    
myPict = makeEmptyPicture(500, 500)
drawLadder(myPict, 50, 30)
