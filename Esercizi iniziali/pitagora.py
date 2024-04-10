def pitagora(cat1, cat2) : 

    # @param cat1 : float (primo cateto)
    # @param cat2 : float (secondo cateto)
    
    cat1 = cat1 ** 2 
    cat2 = cat2 ** 2
    ipo = sqrt(cat1 + cat2)
    
    print 'Valore primo cateto: ', cat1
    print 'Valore secondo cateto: ', cat2
    print 'Valore ipotenusa: ', ipo


a = 4.0
b = 3.3
pitagora(a, b)
