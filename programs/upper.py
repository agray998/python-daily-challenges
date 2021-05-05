def upper_letters(string):
    upperletters = []
    for i in range(0,len(string)):
        char = string[i]
        if char.isalpha() and char == char.upper():
            upperletters.append((char,i))
        else:
            pass
    return upperletters
            
