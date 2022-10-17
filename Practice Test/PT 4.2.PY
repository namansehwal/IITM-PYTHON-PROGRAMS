n=int(input())
l=input().split(",")
x=len(l)
for i in range(x):
    l[i]=int(l[i])
    for j in range(i+1, x):
        l[j]=int(l[j])
        if(l[i]<l[j]):
            l[i], l[j]=l[j], l[i]
sum=0
count=0
for i in l:
    sum+=i
    count+=1
    if(sum>=n):
        print(count)
        break
else:
    print("None")