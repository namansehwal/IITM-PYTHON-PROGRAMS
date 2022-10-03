T = int(input())
for i in range(T):
  x = input()
  z = 0
  y = 0
  for j in range(len(x)):
    z = x.count("0")
    y = x.count("1")
  if y > z:
    print("WIN")
  else:
    print("LOSE")