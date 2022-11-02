list(map(int,input().split(',')))
coins = list(map(int,input().split(',')))
#123456
mapping = { 
            1:0,
            2:0,
            3:0,
            4:0,
            5:0
          }
size = len(coins)//5
for i in range(size):
    