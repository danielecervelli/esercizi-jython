def deleteMultiples(L, j):
    
    # @param L: list
    # @param j: int
    # @return list
    
    newList = []
    
    for i in range(0, len(L)):
        if L[i] % 2 != 0 :
            newList.append(L[i])
    print newList
    return newList
    
    
L = [123, 3, 6, 2, 7, 18]
deleteMultiples(L, 2)