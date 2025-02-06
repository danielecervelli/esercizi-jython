def remove(A, s):
    
    # @param A: list
    # @param s: string
    # @return list
    
    new_list = []
    
    for i in range(0, len(A)):
        if A[i][0] != s[-1]:
            new_list.append(A[i])
    return new_list


A = ['aac','bb','acc','cda','ec']
remove(A, 'ca')