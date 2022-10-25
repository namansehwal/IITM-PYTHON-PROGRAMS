L = input().split(',')
real_dict = dict()
for word in L:
    start = word[0]
    if start not in real_dict:
        [start] = [ ]
    real_dict[start].append(word)