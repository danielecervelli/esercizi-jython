def count(list, element):
    
    # @param list: list of elements
    # @param element: list item
    # return int
    
    times = 0
    
    for i in range(len(list)):
        
        if(list[i] == element):
            times += 1
    
    return times
