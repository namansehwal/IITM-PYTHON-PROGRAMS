n=int(input())
d=[]
for i in range(n):
    list=[int(a) for a in input().split()]
    d.append(list)
c=int(input())
for i in d:
    e=[]
    for j in i:
        e.append(j*c)
    print(*e)