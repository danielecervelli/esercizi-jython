def replaceChar(s):
    
    # @param s: string
    # return string
    
    for i in range(0, len(s)):
    
        if (s[i] in s[:i] and s[i] != ' '):
            s = s[:i] + '*' + s[i+1:]
    
    return s  
    