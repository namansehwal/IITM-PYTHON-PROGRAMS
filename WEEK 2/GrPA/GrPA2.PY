a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input()) 

sum = a+b+c+d+e

condition = ((a+b)%2 ==0) and ((b+c)%2 ==0) and ((c+d)%2 ==0) and ((d+e)%2 ==0) and ((e+a)%2 ==0)


if condition:
    print('YES')
else:
    print('NO')    