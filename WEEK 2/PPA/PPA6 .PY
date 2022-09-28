string = input()
if len(string)%2 == 0:
    if string[-1] == '.':
        string = string[0:-1]
    else:
        string = string+'.'
     
x =len(string)//2             
print(string[x-1:x+2])
