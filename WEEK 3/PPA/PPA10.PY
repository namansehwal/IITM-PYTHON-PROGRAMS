#Accept a positive integer nn as input and print the sum of all prime numbers in the range [1, n][1,n], endpoints inclusive. If there are no prime numbers in the given range, then print 0.
n = int(input())
sum = 0
for i in range(2, n+1):
    if i == 2 or i%2 != 0:
        if n % i == 0:
            sum = sum + i
            # n = n / i
print(sum)

