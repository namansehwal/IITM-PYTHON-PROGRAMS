def factors(n):
    temp = set()
    for x in range(1,n+1):
         if n%x == 0:
            temp.add(x)
    return temp        

def common_factors(a, b):
    a = factors(a)
    b = factors(b)
    return a.intersection(b)

def factors_upto(n):
    D = dict()
    for i in range(1, n + 1):
        D[i] = factors(i)
    return D 
    