n=input()
flag=True
if((int(n[0])<=5)or(len(n)<10)):
    flag=False
for i in range(0, len(n)):
        if((n.count(n[i])>7)or(n[i]*6 in n)):
            flag=False
if flag:
    print("valid")
else:
    print("invalid")