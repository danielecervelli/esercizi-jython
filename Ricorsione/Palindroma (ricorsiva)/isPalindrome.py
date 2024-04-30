def isPalindrome(str):
      
      # @param str: string
      # return boolean
      
      lenght = len(str)
      
      if lenght == 0 or lenght == 1:
          return True
      
      if str[0] == str[lenght - 1]:
          return isPalindrome(str[1:lenght - 1])
      else:
          return False