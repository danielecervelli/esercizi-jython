def decimalToBinary(B, n):

    # @param B: int
    # @param n: int
    # return: list of int
    
    list = []
    while (n > 0):
        list.append(n % B)
        n = (n / B)
    
    list.reverse()
    return list
  