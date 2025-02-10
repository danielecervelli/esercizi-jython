def equalDigAlp(s, counter_d, counter_a):
    
    if len(s) == 0:
        return counterD == counterA
    
    if s[0].isdigit():
        counterD += 1
    elif s[0].isalpha():
        counterA += 1
        
    return equalDigAlp(s[1:], counterD, counterA)
        
print(equalDigAlp("aa336", 0, 0))