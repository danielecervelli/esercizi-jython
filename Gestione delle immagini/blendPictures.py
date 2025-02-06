def mixer(pict1, pict2):
    
    # @param pict1: picture
    # @param pict2: picture
    
    W = min(getWidth(pict1), getWidth(pict2))
    H = min(getHeight(pict1), getHeight(pict2))
    canvas = makeEmptyPicture(W, H)
    
    for b in range(0, 101, 5):
    
        blendPictures(pict1, pict2, b, canvas)
        repaint(canvas)


def blendPictures(pict1, pict2, blendFactor, canvas):
    
    # @param pict1: picture
    # @param pict2: picture
    # @param blendFactor: int (0 <= blendFactor <= 100)
    # @param canvas: picture
    
    for x in range(0, getWidth(canvas)):
        for y in range(0, getHeight(canvas)):
            
            pixCanvas = getPixel(canvas, x, y)
            pix1 = getPixel(pict1, x, y)
            pix2 = getPixel(pict2, x, y)
            
            newRed = (blendFactor / 100.0) * getRed(pix1) + (1 - (blendFactor / 100.0)) * getRed(pix2)
            newGreen = (blendFactor / 100.0) * getGreen(pix1) + (1 - (blendFactor / 100.0)) * getGreen(pix2)
            newBlue = (blendFactor / 100.0) * getBlue(pix1) + (1 - (blendFactor / 100.0)) * getBlue(pix2)
            
            color = makeColor(newRed, newGreen, newBlue)
            setColor(pixCanvas, color)
