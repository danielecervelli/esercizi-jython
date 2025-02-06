def move(t, i, j):
    
    # @param t: tuple
    # @param i: int
    # @param j: int
    # @return tuple
    
    if i >= len(t):
        print "posizione i non esiste nella tupla"
        print t
        return -1
        
    if j >= len(t):
        print "posizione j non esiste nella tupla"
        print t
        return -1
    
    print t
    temp = list(t)
    
    value1 = temp[i]
    value2 = temp[j]
    temp[i] = value2
    temp[j] = value1
    
    new_t = tuple(temp)
    print new_t
    
    
t = (5, 8, 1, 7, 10)
move(t, 0, 5)