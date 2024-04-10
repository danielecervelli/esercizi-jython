def swapRedGreen(pict):
    
    # @param pict: picture
    
    allPixels = getPixels(pict)
    
    for i in range(0, len(allPixels)):
    
        redValue = getRed(allPixels[i])
        greenValue = getGreen(allPixels[i])
        
        setRed(allPixels[i], greenValue)
        setGreen(allPixels[i], redValue)
        
    repaint(pict)


myPict = makeEmptyPicture(400, 400, red)
swapRedGreen(myPict)
