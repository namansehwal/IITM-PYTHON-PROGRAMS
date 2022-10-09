a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a<=b and a<=c and a<=d):
    if(b<=c and b<=d):
        if(c<=d):
            print(a,b,c,d)
        else:
            print(a,b,d,c)
    elif(c<=b and c<=d):
        if(b<=d):
            print(a,c,b,d)
        else:
            print(a,c,d,b)
    else:
        if(b<=c):
            print(a,d,b,c)
        else:
            print(a,d,c,b)
elif(b<=a and b<=c and b<=d):
    if(a<=c and a<=d):
        if(c<=d):
            print(b,a,c,d)
        else:
            print(b,a,d,c)
    elif(c<=a and c<=d):
        if(a<=d):
            print(b,c,a,d)
        else:
            print(b,c,d,a)
    else:
        if(a<=c):
            print(b,d,a,c)
        else:
            print(b,d,c,a)
elif(c<=a and c<=b and c<=d):
    if(a<=b and a<=d):
        if(b<=d):
            print(c,a,b,d)
        else:
            print(c,a,d,b)
    elif(b<=a and b<=d):
        if(a<=d):
            print(c,b,a,d)
        else:
            print(c,b,d,a)
    else:
        if(a<=b):
            print(c,d,a,b)
        else:
            print(c,d,b,a)
else:
    if(a<=b and a<=c):
        if(b<=c):
            print(d,a,b,c)
        else:
            print(d,a,c,b)
    elif(b<=a and b<=c):
        if(a<=c):
            print(d,b,a,c)
        else:
            print(d,b,c,a)
    else:
        if(a<=b):
            print(d,c,a,b)
        else:
            print(d,c,b,a)