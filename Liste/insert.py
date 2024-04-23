def insert(L, n1, n2):

    # @param L: list of int numbers
    # @param n1: int number
    # @param n2: int number
    # return list
    
    newList = []
    
    for i in range(0, len(L)):
        
        if(L[i] == n1):
            newList.append(L[i])
            newList.append(n2)
        else:
            newList.append(L[i])            
    
    return newList
