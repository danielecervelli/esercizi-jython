def printMatrix(matrix):
    
    # @param matrix: list of lists
    
    for i in range(0,len(matrix)):
        print matrix[i]
        

def swapRowCol(mat, x):

    # @param mat: list of lists
    # @param x: int
    
    if x < 0 or x > len(mat):
        return -1
    
    newList = []
    for i in range(len(mat)):
    
        newList.append(mat[x][i])
        mat[x][i] = mat[i][x]
        mat[i][x] = newList[i]
        
    printMatrix(mat)
