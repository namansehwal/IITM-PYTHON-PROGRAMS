a, b, c = 0, 0, 0
A, B, C = True, True, True
if A:
    a += 1
    if B:
        a += 1
        b += 1
        if C:
            a += 1
            b += 1
            c += 1
print(a + b + c)