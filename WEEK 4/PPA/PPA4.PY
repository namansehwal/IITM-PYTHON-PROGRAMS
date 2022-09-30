L = input().split(',')
max =''
for word in L:
    if len(word) >= len(max):
        max = word
print(max)        