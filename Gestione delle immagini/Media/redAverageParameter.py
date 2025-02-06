def redAverageParameter(pict, k):

    # @param pict: picture
    # @param k: int
    
    sum = 0
    count = 0
    
    for x in range(0, getWidth(pict)):
        for y in range(0, getHeight(pict)):
        
            pix = getPixel(pict, x, y)
        
            if (x <= k):
                redValue = getRed(pix)
                sum += redValue
                count += 1
    
    result = sum / count
    
    print result


myPict = makeEmptyPicture(500, 500, red)
redAverageParameter(myPict, 50)
