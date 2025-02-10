def checkRow(A):

    # @param A: pict
    # @return bool

    counter = 0
    
    for y in range(1, getHeight(A)):
        for x in range(0, getWidth(A)):
            
            pix1 = getPixel(A,x,y)
            pix2 = getPixel(A,x,y-1)
            pix1_color = getColor(pix1)
            pix2_color = getColor(pix2)
            
            if pix1_color == pix2_color:
                counter += 1

            if counter == getWidth(A):
               return True

    return False

pict = makeEmptyPicture(50,50, red)
print(checkRow(pict))