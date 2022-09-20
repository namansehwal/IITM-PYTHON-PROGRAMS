n1=str(input())
d1=str(input())
n2=str(input())
d2=str(input())

if(d1[6:10] == d2[6:10]):
    if(d1[3:5] == d2[3:5]):
        if(d1[0:2] == d2[0:2]):
            if(n1<n2):
                print(n1)
            else:
                print(n2)
        elif(d1[0:2] > d2[0:2]):
            print(n1)
        else:
            print(n2)
    elif(d1[3:5] > d2[3:5]):
        print(n1)
    else:
        print(n2)
elif(d1[6:10] > d2[6:10]):
    print(n1)
else:
    print(n2)