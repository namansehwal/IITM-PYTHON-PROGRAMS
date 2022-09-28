string = input().lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

output = ""

for a in alphabet:
    if a in string:
        output += a * string.count(a)

print(output)