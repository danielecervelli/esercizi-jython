def printMatrix(M):
    
    # @param M: matrix
    
    for i in range(0, len(M)):
        print M[i]


def swapMatValues(M, h):
    
    # @param M: matrix
    # @param h: int
    
    lenght = len(M)
    
    if len(M[0]) != lenght:
        printMatrix(M)
        print "Matrice non quadrata"
        return -1
    
    if h > len(M[0]) or h > lenght:
        printMatrix(M)
        print "Index error"
        return -1
    
        
    newRow = []
    newCol = []
    
    for i in range(0, lenght):
        newRow.append(M[i][h])
        newCol.append(M[h][i])
    
    for j in range(0, lenght):
        M[j][h] = newCol[j]
        M[h][j] = newRow[j]
    
    printMatrix(M)
    return M


M = [[1, 2, 3],
    [3, 5 , 7],
    [3, 5 , 7]]
    
swapMatValues(M, 2)