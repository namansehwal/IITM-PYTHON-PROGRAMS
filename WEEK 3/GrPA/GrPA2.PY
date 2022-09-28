n = int(input())
for i in range(2, n+1):
  if i == 2 or i%2 != 0:
    if n % i == 0:
        print(i)
        n = n / i




