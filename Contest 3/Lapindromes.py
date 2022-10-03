for _ in range(int(input())):
    
    s = input()
    l = len(s)//2
    if (sorted(s[0:l])) == sorted(''.join(reversed(s[-l:]))):
        print('YES')
    else:
        print('NO')   
  