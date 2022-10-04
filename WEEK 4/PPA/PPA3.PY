n = input()
L = n.split(',')
max = -1
for x in L:
  if int(x) > max:
    max = int(x)
print(max)