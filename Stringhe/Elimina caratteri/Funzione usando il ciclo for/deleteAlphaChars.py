def deleteAlphaChars(str):
    
    # @param str: string
    # return string
    
    newStr = ''
    
    for i in range(0, len(str)):
        
        if str[i].isdigit() or str[i] == ' ':
            newStr += str[i]
    
    return newStr
