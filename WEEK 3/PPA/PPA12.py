a=str(input())
b=str(input()) 
c=""
for i in b:
    flag=True
    if i in a:
        Flag=False
    else:
        c+=i
        flag=True
        
print(c)