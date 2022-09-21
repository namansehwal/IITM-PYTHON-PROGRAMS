string = input()
if len(string)%2 == 0:
    if string[-1] == '.':
        string.replace('.','',-1)
    else:
        string.join('.')
word = string            
print(word)