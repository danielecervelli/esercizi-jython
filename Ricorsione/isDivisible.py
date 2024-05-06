def isDivisible(num):
    
    # @param num: int
    # return bool
    
    if (num < 10):
        if (num in [3, 6, 9]):
            return True  
        else:
            return False
    else:
        sum = 0
        s = str(num)
        
        for i in range(len(s)):
            sum += int(s[i])
        
        return isDivisible(sum)
        
