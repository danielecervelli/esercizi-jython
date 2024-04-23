def myFind(s, c):

    # @param s: string
    # @param c: string
    # return string
    
    for i in range(0,len(s)):
        
          if (c in s[i:len(c) + i]):
             return i
          
    return -1 
    