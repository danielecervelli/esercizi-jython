def drawRectangle(pict, startX, startY, width, height):

    # @param pict: picture
    # @param startX: int
    # @param startY: int
    # @param width: int
    # @param height: int
    
    for i in range(0, width):
        for j in range(0, height):
            pixel = getPixel(pict, startX + i, startY + j)
            setColor(pixel, black)
            
    repaint(pict)


myPict = makeEmptyPicture(500, 500)
drawRectangle(myPict, 0, 0, 300, 100)