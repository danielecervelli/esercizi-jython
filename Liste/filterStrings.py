def filterStrings(L):
    # @param L: list of strings
    # @return list
    
    if not L:
        return []
    
    firstStr = L[0]
    
    if len(firstStr) > 0 and firstStr[0] == firstStr[-1]:
        print L
        return [firstStr] + filterStrings(L[1:])
    else:
        print L
        return filterStrings(L[1:])

L = ["abc", "dd", "c", "ghig", "ab"]
print(filterStrings(L))