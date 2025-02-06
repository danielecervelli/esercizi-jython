def darkenImage(pict):

    # @param pict: picture
    
    allPixels = getPixels(pict)
        
    for i in range(0, 10):
        for j in range(0, len(allPixels)):
            
            myRed = getRed(allPixels[j]) - 26
            myGreen = getGreen(allPixels[j]) - 26
            myBlue = getBlue(allPixels[j]) - 26
            
            newColor = makeColor(myRed, myGreen, myBlue)
            setColor(allPixels[j], newColor)
        
        repaint(pict)
        
        
myPict = makeEmptyPicture(300, 300)
darkenImage(myPict)
