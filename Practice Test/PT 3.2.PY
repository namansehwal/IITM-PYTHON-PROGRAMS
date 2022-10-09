num1=int(input())
num2=int(input())
x=min(num1, num2)
for i in range(1, x):
    if (num1%i==0 and num2%i==0):
        hcf=i
if (hcf==1):
    print("Coprime")
else:
    print("Not Coprime")