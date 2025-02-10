def sum(n):
    
    # @param n: int
    # @return int
    
    if n == 1:
        return 1
    else:
        print n
        return n + sum(n - 1)