n = int(input())
A = []
B = []
for i in range(n):
    A.append(list(map(int,input().split(","))))
for i in range(n):
    B.append(list(map(int,input().split(","))))
C = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k]*B[k][j]
for i in range(n):
    print(",".join(map(str,C[i])))
