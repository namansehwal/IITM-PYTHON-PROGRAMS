L = input().split(' ')
	# there is a single space between the quotes
# print(L)
for i in range(len(L) - 1):
    if len(L[i]) > len(L[i + 1]):
        L[i], L[i + 1] = L[i + 1], L[i]

count = 0
print(L)
for i in range(len(L)):
    if len(L[i]) <= len(L[-1]):
        count += 1

print(count)