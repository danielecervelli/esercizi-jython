def countC(s,c,n):
    
    # @param s: string
    # @param c: string
    # @param n: int
    # @return bool
    
    if len(c) != 1:
        return -1
    
    if n == 0:
        print "ok"
        return True
        
    if not s:
        print "not ok"
        return False
        
    if s[0] == c:
        return countC(s[1:],c,n-1)
    else:
        return countC(s[1:],c,n)
        
count_c("aanjbnka", "a", 9)