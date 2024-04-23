def deleteNumbers(str):
    
    # @param str: string
    # return string
    
    newStr = ''
    
    for i in range(0, len(str)):
        
        if str[i].isalpha() or str[i] == ' ': 
            newStr += str[i]
    
    return newStr