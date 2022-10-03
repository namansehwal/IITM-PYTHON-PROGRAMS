T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    R = input()

    if S.count('0') == R.count('0') and S.count('1') == R.count('1'):
        print("YES")
    else:
         print("NO")
