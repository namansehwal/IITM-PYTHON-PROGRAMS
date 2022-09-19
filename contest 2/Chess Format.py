TestCases = int(input())

for _ in range(TestCases):
    A, B = [int(x) for x in input().split()]
    sum = A+B

    #conditions
    if sum<3:
        print(1)
    elif 3 <=sum <=10:
        print(2)
    elif 11 <=sum <=60:
        print(3)
    elif 3 < sum:
        print(4)    
