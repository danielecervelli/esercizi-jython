def redAverage(pict):

    # @param pict: picture
    
    allPixels = getPixels(pict)
    numPixels = len(allPixels)
    
    sum = 0
    for i in range(0, numPixels):
         redValue = getRed(allPixels[i])
         sum += redValue
    
    result = sum / numPixels
    print 'Media valori dei pixel rossi:', result


myPict = makeEmptyPicture(400, 400, red)
redAverage(myPict)
