lists = ['132', '123', '124', '130', '131']

l=list(map(float,input().split(',')))

l2=[]

for i in range(len(l)):
    min=l[i]
    # for j in range(len(l)):
    if min>l[j]:
        min=l[j]
        # else:
        #     continue
    # l.remove(min)
    l2.append(min)
print(l2)