def extractRows(M, k):
    
    # @param M: matrix
    # @param k: int
    # @return list
    
    list = []
    for x in range(0, len(M)):
        for y in range(0, len(M[0])):    
            if x < k:
                list.append(M[x][y])
    print list
    return list
    
    
M = [
    [1, 2, 3, 10],
    [3, 5 , 7, 2],
    [4, 9, 2, 5]
    ]
extractRows(M, 2)