n=int(input())
a=[]
b=[]
for i in range(2):
    for j in range(n):
        f=[]
        f=input().split(',')
        for k in range(n):
            f[k]=int(f[k])
        if i==0:
            a.append(f)
        else:
            b.append(f)
for i in range(n):
    for j in range(n):
        a[i][j]+=b[i][j]
        if j<n-1:
            print(a[i][j],end=',')
        else:
            print(a[i][j])