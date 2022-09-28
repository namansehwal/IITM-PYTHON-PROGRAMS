n = int(input())

sum = 0
i = 0

while i <= n:
    j = 1
    while j <= i:
        sum += j
        j += 1
    i += 1

print(sum)