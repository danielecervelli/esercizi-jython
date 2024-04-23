def deleteAlpha(str):

    # @param str: string
    # return string
    
    newStr = ''
    
    i = 0
    while(i != len(str)):
 
        if not str[i].isalpha():
            newStr += str[i]
        i += 1

    return newStr
    