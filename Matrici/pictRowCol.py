def swapRowCol(pict, x):
    
    # @param pict: picture
    # @param x: int
    
    if getWidth(pict) != getHeight(pict):
        return -1
    
    if x < 0 or x > getWidth(pict-1):
        return -1
    
    for i in range(getHeight(pict)):
    
        pixel1 = getPixel(pict,x,i)
        pixel2 = getPixel(pict,i,x)
        
        color1 = getColor(pixel1)
        color2 = getColor(pixel2)
        
        setColor(pixel1,color2)
        setColor(pixel2,color1)
        
    repaint(pict)
