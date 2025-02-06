def sum(M):
    
    # @param M: matrix
    # @return int
    
    result = 0
    for i in range(0, len(M)):
        for j in range(0, len(M[0])):
            if i % 2 == 0:
                result += M[i][j]
            if j % 2 != 0:
                result += M[i][j] 
    print result
    return result
           
M = [
    [1, 2, 3],
    [3, 5 , 7],
    [4, 9, 2]
    ]
sum(M)