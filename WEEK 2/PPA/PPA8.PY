a=str(input())
b=str(input())
dictt = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8'}
num1=int(dictt[a[0]])
num2=int(a[1])
num3=int(dictt[b[0]])
num4=int(b[1])
if num1+num2 == num3+num4 or num2-num1==num4-num3 :
    print("YES")
else:
    print("NO")
