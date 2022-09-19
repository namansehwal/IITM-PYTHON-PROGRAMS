TestCases = int(input())

for _ in range(TestCases):
    x1,x2,y1,y2,z1,z2 = [int(x) for x in input().split()]
    
    #conditions
    if (20<=x1<=50 and 20<=x2<=50) and (1900<=y1<=2100 and  1900<=y2<=2100) and (1<=z1<=6 and  1<=z2<=6):
               print('YES')
    else:
        print('NO')
       
