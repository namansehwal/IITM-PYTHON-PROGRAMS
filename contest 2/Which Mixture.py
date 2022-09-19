TestCases = int(input())

for _ in range(TestCases):
    A, B = [int(x) for x in input().split()]
    
    #conditions
    if A>0 and B>0: print('solution')
    elif B == 0 and B>0: print('solid')
    else: print('liquid')

# for _ in range(int(input())):
#   n,m = map(int,input().split())
#   if (n > 0 and m > 0):
#     print('Solution')
#   elif n == 0 and m > 0:
#     print('Liquid') 
#   else:
#     print('Solid')
