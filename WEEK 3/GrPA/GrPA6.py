n = int(input())

# first half
for i in range(1, n + 2):
    for j in range(1, i):
        # check for entry
        if j < i - 1:
            print(j, end=",")
        else:
            print(j)
# second half
for i in range(n, 0, -1):
    for j in range(1, i):
        # check for last entry
        if j < i - 1:
            print(j, end=",")
        else:
            print(j)