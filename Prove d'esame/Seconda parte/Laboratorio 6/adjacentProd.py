def adjacentProd(M, h, k):

    # @param M: matrix
    # @param h: int
    # @param k: int
    # @return int
    
    result = 1
    flag = False

    if k - 1 >= 0:
        result *= M[h][k - 1]
        elemExist = True

    if k + 1 < len(M[0]):
        result *= M[h][k + 1]
        elemExist = True

    if elemExist:
        print result
        return result
    else:
        return -1
    
    
M = [
    [1, 2, 3, 10],
    [3, 5, 7, 2],
    [4, 9, 2, 5]
    ]
adjacentProd(M, 1, 3)