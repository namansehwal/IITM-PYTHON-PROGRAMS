word = 'aaabeeedee'
valid = True
for i in range(len(word)):
    char = word[i]
    if i % 2 == 0 and char not in 'aeiou':
        valid = False
print(valid)