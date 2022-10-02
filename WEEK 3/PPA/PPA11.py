c=int(input())
flag=True
for x in range (1, c):
    for y in range (1, c):
        for z in range(1, c):
            if x*x + y*y == z*z and (x<y) and (y<z) and (z<c):
                print (x, y, z,sep=",")
                flag=False

if flag:
    print("NO SOLUTION")