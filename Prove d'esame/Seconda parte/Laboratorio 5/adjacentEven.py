def adjacentEven(mat, i, j):
    
    # @param mat: matrix
    # @param i: int
    # @param j: int
    # @return bool
 
    rows = len(mat)
    cols = len(mat[0])
    
    adjacent = []
    
    if i > 0:
        adjacent.append(mat[i-1][j])
    if i < rows - 1:
        adjacent.append(mat[i+1][j])
    if j > 0:
        adjacent.append(mat[i][j-1])
    if j < cols - 1:
        adjacent.append(mat[i][j+1])
    
    for x in adjacent:
        if x % 2 != 0:
            return False
    return True


mat = [
        [2, 3, 4],
        [6, 5, 8],
        [10, 12, 14]
        ]
print(adjacentEven(mat, 1, 1))