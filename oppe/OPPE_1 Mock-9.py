coins =input()
L = len(coins)
box = [0,0,0,0,0]
for i in range (0,L):
    box[i%5] += int(coins[i])
print(box.index(max(box))+1)