def replaceChars(s):
    
    # @param s: string
    # return string
    
    charCount = {}
    newStr = ''

    for char in s:
        
        if char != ' ':
            if char not in charCount:
                charCount[char] = 1
                newStr += char
            elif charCount[char] == 1:
                charCount[char] += 1
                newStr += ''
        else:
            newStr += ' '

    return newStr