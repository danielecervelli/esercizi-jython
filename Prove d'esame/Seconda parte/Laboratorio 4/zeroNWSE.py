def printMat(M):

    # @param M: matrix
    
    for i in range(len(M)):
        print M[i]


def zeroNWSE(A, h, k):

    # @param A: matrix
    # @param h: int
    # @param k: int
    # @return matrix

    m = len(A)
    n = len(A[0])
    
    if h > 0:
        A[h-1][k] = 0
    if h < m - 1:
        A[h+1][k] = 0
    if k > 0:
        A[h][k-1] = 0
    if k < n - 1:
        A[h][k+1] = 0
    
    printMat(A)
    return A
    
    
A = [
    [1,3,4,10],
    [3,4,6,3],
    [6,7,6,7]
    ]
zeroNWSE(A,0,0)