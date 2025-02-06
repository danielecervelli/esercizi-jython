def swapRedMinBlue(pict):

    # @param pict: picture
    
    allPixels = getPixels(pict)
    lenght = len(allPixels)
    
    for i in range(0, lenght):
        
        redValue = getRed(allPixels[i])
        blueValue = getBlue(allPixels[i])
        
        if(redValue < blueValue):
            setRed(allPixels[i], blueValue)
            setBlue(allPixels[i], redValue)
            
    repaint(pict)
        
    
myPict = makeEmptyPicture(500, 500, blue)
swapRedMinBlue(myPict)
