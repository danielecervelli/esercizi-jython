def float10ToBinary(B, n, precision):
    
    # @param B: int
    # @param n: float
    # @param precision: int
    # return: list of int
    
    list = []
    i = 0
    while (n > 0 and i < precision):
        list.append(int(n * B))
        n = (n * B) - (int(n * B))
        i += 1
  
    list.reverse()  
    return list
    