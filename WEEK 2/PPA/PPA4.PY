p = int(input())
h = int(input())
b = int(input())
if (p*p+h*h==b*b) or(b*b+p*p==h*h) or(h*h+b*b==p*p):
    print('YES')
else:
    print('NO')    