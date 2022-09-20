x = float(input())
y = float(input())

if (0<x and 0<y):
    print('first')
elif (0>x and 0<y):
    print('second')
elif (0>x and 0>y):
    print('third') 
elif (0<x and 0>y):
    print('fourth')
elif (x== 0 and y== 0):
    print('origin')
elif (x!=0 and y==0):
    print('x-axis') 
elif (y!=0 and x==0):
    print('y-axis')                         