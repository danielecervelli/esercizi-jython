def swapRedBlue(pict, k):

    # @param pict: picture
    # @param k: int
    
    for x in range(0, k):
        for y in range(0, getHeight(pict)):
            
            pix = getPixel(pict, x, y)
        
            redValue = getRed(pix)
            blueValue = getBlue(pix)
            
            setRed(pix, blueValue)
            setBlue(pix, redValue)
            
    repaint(pict)
    
    
myPict = makeEmptyPicture(500, 500, red)
swapRedBlue(myPict, 300)
