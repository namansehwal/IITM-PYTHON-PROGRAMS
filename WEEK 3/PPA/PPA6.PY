flag = True
n = input()
max = n
while flag:
    n = input()
    if n == 'abcdefghijklmnopqrstuvwxyz':
        flag = False
    else:
         
        if len(n)<len(max):
            max = n 
print(max) 