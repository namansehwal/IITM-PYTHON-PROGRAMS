n = int(input())
final = []
for i in range(n):
    temp = []
    for j in range(n):
        if i == j:
            temp.append(1)
        else:
            temp.append(0)
    final.append(temp)        
for i in final:
    print(*i,sep=',')    
    