
string = input().split()
word = input()
if word in string:
    print("YES")
    print(string.count(word))
else:
    print("NO")
    exit()
        
    