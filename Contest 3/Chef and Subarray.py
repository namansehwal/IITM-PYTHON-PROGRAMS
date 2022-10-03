input()

list = [int(a) for a in input().split()]

count = 0
max = 0
for x, y in enumerate(list):
        if list[x]*y != 0:
            count += 1
        else:
            count = 0
        if max < count:
            max = count
print(max)
