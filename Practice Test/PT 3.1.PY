string = input()

flag =True

for x in range(len(string)//2):
    if string[x] != string[-x-1]:
        print("NOT PALINDROME")
        flag = False
        break
if flag:
    print("PALINDROME")
        
        