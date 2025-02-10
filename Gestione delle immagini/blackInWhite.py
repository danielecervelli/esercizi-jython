def blackInWhite(pict):
    
    counter = 0
    sum = 0
    
    for x in range(0, getWidth(pict)):
        for y in range(0, getHeight(pict)):
            pix = getPixel(pict, x, y)
            
            if getColor(pix) == black:
                counter += 1
                sum += 1
            
        if counter == sum:
            for i in range(0, getHeight(pict)):
                pix = getPixel(pict, x, i)
                setColor(pix, white)

pict = makeEmptyPicture(100, 100, black)
show(pict)
blackInWhite(pict)
repaint(pict)