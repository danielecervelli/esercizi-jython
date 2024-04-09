def swapRedGreen(pict):
    
    # @param pict: picture
    
    allPixels = getPixels(pict)
    
    for i in range(0, len(allPixels)):
        redPixel = getRed(allPixels[i])
        greenPixel = getGreen(allPixels[i])
        
        setRed(allPixels[i], greenPixel)
        setGreen(allPixels[i], redPixel)


myPict = makeEmptyPicture(400, 400, red)
swapRedGreen(myPict)
show(myPict)
