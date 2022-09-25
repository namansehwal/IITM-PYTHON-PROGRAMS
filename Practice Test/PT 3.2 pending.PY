from re import A


a = int(input())
b = int(input())


if a%b!=0 and b%a!=0:
    print("Coprime")
else:
    print('Not Coprime')   