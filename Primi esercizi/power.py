def power(base, exponent):
    
    # @param base: int
    # @param exponent: int
    
    if exponent == 0:
        print "Risultato = 1"
        return 1
    
    for i in range(0, exponent):
        result = base * base
    return result
    