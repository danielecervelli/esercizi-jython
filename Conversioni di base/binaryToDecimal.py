def binaryToDecimal(B, n):
    
    # @param B: int
    # @param n: list of int
    # return: int

    number = 0
    n.reverse()
    
    for i in range(0, len(n)):
        number = number + n[i] * B ** i
    
    return number
