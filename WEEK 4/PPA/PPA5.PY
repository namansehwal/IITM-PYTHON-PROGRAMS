n = input().split()
final = []
for num in n:
    temp = num.split('.')
    final.append(temp[0])
print(*final,sep = ',')
    