def maxLenght2(str1, str2, str3):

    # @param str1: string
    # @param str2: string
    # @param str3: string
    # return string
    
    if(len(str1) >= len(str2)) and (len(str1) >= len(str3)):
        return str1
    
    if(len(str2) >= len(str1)) and (len(str2) >= len(str3)):
        return str2
    
    if(len(str3) >= len(str1)) and (len(str3) >= len(str2)):
        return str3
