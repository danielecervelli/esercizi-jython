def sameColor(A):

    # @param A: picture
    # @return bool
    
    for y in range(0, getHeight(A)):
        
        if searchLine(y, A):
            return True
        return False

def searchLine(i, pict):

    # @param i: int
    # @param pict: picture
    # @return bool
    
    pix = getColor(getPixel(pict), 0, i)
    
    for x in range(0, getWidth(pict)):
        pix2= getColor(getPixel(pic, x, i))
        
        if pix != pix2:
            return False
    return True
            