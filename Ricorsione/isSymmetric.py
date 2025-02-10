def isSymmetric(s):
    
    # @param s: string
    # @return bool
    
    if len(s) <= 1:
        return True
    
    if len(s) % 2 != 0:
        s=s[:len(s) // 2] + s[len(s) // 2 + 1:]
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    if len(s1) == 1:
        return s1[0] == s2[0]
    else:
        return s1[0] == s2[0] and isSymmetric(s1[1:]+s2[1:])