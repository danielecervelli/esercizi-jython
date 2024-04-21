def isPalindrome(str):
    
    # @param str: string
    # return: boolean
    
    lenght = len(str)
    lenght2 = lenght / 2
    
    for i in range(0, lenght2):
        if (str[i] != str[lenght - i - 1]):
            return false
        else:
            return true
