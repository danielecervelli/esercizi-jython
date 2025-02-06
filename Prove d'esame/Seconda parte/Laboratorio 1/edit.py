def edit(M, h, k):

    # @param M: matrix
    # @param h: int
    # @param k: int

    value = M[h][k]
    
    for i in range(0, len(M)):
        if M[i][k] != value:
            M[i][k] *= value
    
    for j in range(0, len(M[h])):
        if M[h][j] != value:
            M[h][j] *= value  
    
    for z in range(0, len(M)):
        print M[z]


M = [
    [1, 2, 6, 10, 20],
    [7, 5, 3, 2 ,7 ],
    [4, 12, 9, 5, 1 ],
    [8, 11, 6, 4, 13]
    ]
edit(M, 1, 2)