def myRfind(str, subStr):

    # @param str: string
    # @param subStr: string
    # return int
    
    for i in range(len(str) - len(subStr), -1, -1):

        if(str[i:i + len(subStr)] == subStr):
            return i
             
    return -1 
    