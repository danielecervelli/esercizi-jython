def maxLenght3(strings):

    # @param strings: list of "n" strings
    # return string
    
    max = len(strings[0])
    pos = 0
    
    for i in range(1, len(strings)):
    
        if(max < len(strings[i])):
            max = len(strings[i])
            pos = i
            
    return strings[pos]
    