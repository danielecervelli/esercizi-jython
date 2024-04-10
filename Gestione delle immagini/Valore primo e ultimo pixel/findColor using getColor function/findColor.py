def findColor(pict):
    
    # @param pict: picture
    
    allPix = getPixels(myPict)
    primoPixel = getColor(min(allPix)) 
    ultimoPixel = getColor(max(allPix))
   
    print 'Colore del primo pixel: \n', primoPixel
    print '\n'
    print 'Colore dell\' ultimo pixel: \n', ultimoPixel


myPict = makePicture(pickAFile())
findColor(myPict)
show(myPict)