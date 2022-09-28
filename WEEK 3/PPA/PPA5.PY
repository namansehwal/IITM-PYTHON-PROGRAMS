flag = True
max = 0
while flag:
    n = int(input())
    if n == 0:
        flag = False
    else:
        if n>max:
            max = n 
print(max)             