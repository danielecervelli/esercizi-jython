def sameBrightness(A):
    
    for y in range(1, getHeight(A)):
      
      if averageBrightness(A,y) != averageBrightness(A,(y-1)):
         return false
    return true
    

def averageBrightness(A, y):
    
    sum = 0
    
    for x in range(0, getWidth(A)):
        sum += getBrightness(A, x, y)
    
    return sum / getWidth(A)


def getBrightness(A, x, y):
    
    pix = getPixel(A,x,y)

    return (getRed(pix) + getBlue(pix) + getGreen(pix))