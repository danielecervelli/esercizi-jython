def stampaPosPari(list):
    
    # @param list: list of numbers
    
    lenght = len(list)
    
    for i in range(0, lenght, 2):
        print list[i]


numbers = [3, 5, 12, 31, 43, 7, 11, 45, 56]
stampaPosPari(numbers)
