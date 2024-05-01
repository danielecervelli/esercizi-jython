def cross(A, i, j):

    # @param A: matrix
    # @param i: int(rows index)
    # @param j: int(columns index)
    # return boolean
    
    printMatrix(A)
  
    if (checkColumns(A, i, j) and checkRows(A, i, j)):
        return True
    else:
        return False


def checkColumns(A, x, y):

    # @param A: matrix
    # @param x: int(rows index)
    # @param y: int(columns index) 
  
    if (x == 0):
        return (A[x][y] >= A[x + 1][y])
    
    elif (x == len(A)-1):
        return (A[x][y] >= A[x - 1][y])
  
    else:
        return (A[x][y] >= A[x - 1][y] and A[x][y] >= A[x + 1][y])


def checkRows(A, x, y):
  
    # @param A: matrix
    # @param x: int(rows index)
    # @param y: int(columns index) 
  
  if (y == 0):
    return (A[x][j] >= A[x][y + 1])
    
  elif (y == len(A) - 1):
    return (A[x][y] >= A[x][y - 1])
  
  else:
    return (A[x][y] >= A[x][y - 1] and A[x][y] >= A[x][y + 1])


def printMatrix(matrix):
    
    # @param matrix: matrix(list of lists)
    
    for i in range(len(matrix)):
        print matrix[i]


A = [1,2,3,10],[3,5,7,2],[4,9,2,5]
