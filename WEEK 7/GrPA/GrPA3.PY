def minor_matrix(M, i, j):
  M.pop(i)
  for x in M:
    x.pop(j)
  return M,i,j  



d = int(input())
x = []
for _ in range(d):
    x.append(input().split(','))
y,z = int(input()),int(input())    
minor_matrix(x,y,z)

print(x)