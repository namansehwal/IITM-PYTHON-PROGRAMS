TestCases = int(input())

for _ in range(TestCases):
    x1,x2,y1,y2,z1,z2 = [int(x) for x in input().split()]
    
    #conditions
    if (x1<=x2) and (y1<=y2) and (z1>=z2):
        print('YES')
    else:
        print('NO')
       

