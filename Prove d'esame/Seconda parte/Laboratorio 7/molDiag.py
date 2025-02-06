def molDiag(A):
    
    # @param A: matrix 
    # @return int
    
    lenght = len(A)
    diag = 1
    antiDiag = 1
    
    for i in range(0, lenght):
        if A[i][i] != 0:
            diag *= A[i][i]
        
        if A[i][lenght-i-1] != 0:
            antiDiag *= A[i][lenght-i-1]
          
    print diag
    print antiDiag
    result = diag * antiDiag
    
    print result
    return result
    

A = [
    [1, 2, 0],
    [3, 5, 7],
    [4, 9, 12]
    ]
molDiag(A)