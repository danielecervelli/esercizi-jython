def myFind(str, subStr):

    # @param str: string
    # @param subStr: string
    # return int
    
    for i in range(0, len(str)):
        
          if(subStr in str[i:len(subStr) + i]):
             return i
             
    return -1 
    