def oddEvenSwap(t):

    # @param t: tuple
    # @return tuple
    
    t_list = list(t)
    
    for i in range(0, len(t) - 1, 2):
        t_list[i], t_list[i + 1] = t_list[i + 1], t_list[i]
    return tuple(t_list)


t = (1, 2, 3, 4, 5, 6, 7)
print(oddEvenSwap(t))  # Output: (2, 1, 4, 3, 6, 5, 7)