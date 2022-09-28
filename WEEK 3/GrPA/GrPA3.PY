flag = True
x= 0
y=0

while flag:
    move = input()
    if move == 'STOP':
        flag = False
    else:
      if(move=="UP"):
        y=y+1
      if(move=="DOWN"):
        y=y-1
      if(move=="LEFT"):
        x=x-1
      if(move=="RIGHT"):
        x=x+1
Distance=(abs(x))+(abs(y))
print(Distance)