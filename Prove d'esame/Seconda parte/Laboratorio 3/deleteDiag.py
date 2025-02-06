def printMat(mat):

    # @param mat: matrix
    
    for j in range(0, len(mat)):
        print mat[j]


def deleteDiag(M):
    
    # @param M: matrix
    
    for i in range(0, len(M)):
        M[i][i] = "*"
        M[len(M)-i-1][i] = "*"
    printMat(M)


M = [[1, 2, 3, 10, 7],
    [3, 5, 7, 2, 1],
    [4, 9, 2, 5, 4],
    [6, 8, 1, 9, 3],
    [5, 2, 3, 6, 2]]    
deleteDiag(M)