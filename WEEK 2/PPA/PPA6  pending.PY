string = input()
if len(string)%2 == 0:
    if string[-1] == '.':
        string = string[0:-1]
    else:
        string = string+'.'
            
print(string)
