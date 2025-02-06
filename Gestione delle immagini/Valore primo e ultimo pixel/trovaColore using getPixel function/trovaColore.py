def trovaColore(pict):

    # @param pict: picture
    
    allPix = getPixels(myPict)

    print 'Colore del primo pixel: \n',  min(allPix)
    print '\n'
    print 'Colore dell\' ultimo pixel: \n', max(allPix)


myPict = makePicture(pickAFile())
trovaColore(myPict)
show(myPict)        