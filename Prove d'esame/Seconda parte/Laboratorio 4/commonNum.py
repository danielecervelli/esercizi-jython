def commonNum(t1, t2):
    
    # @param t1: tuple
    # @param t2: tuple
    # @return tuple
    
    if len(t1) < len(t2):
        lenght = len(t1)
    elif len(t1) > len(t2):
        lenght = len(t2)
    else:
        lenght = len(t1)
    
    newTuple = []
    
    for i in range(0, lenght):
        if t1[i] == t2[i]:
            newTuple.append(t1[i])
    return tuple(newTuple)
        

t1 = (5, 2, 4, 9, 1, 7, 6, 3)
t2 = (4, 2, 7, 9, 1)
commonNum(t1, t2)