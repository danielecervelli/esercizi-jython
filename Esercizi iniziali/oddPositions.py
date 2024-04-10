def oddPositions(list):
    
    # @param list: list of numbers
    
    lenght = len(list)
    
    for i in range(1, lenght, 2):
        print list[i]


numbers = [3, 5, 12, 31, 43, 7, 11, 39, 43, 56]
oddPositions(numbers)
