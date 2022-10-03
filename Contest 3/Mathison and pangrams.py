alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for _ in range(int(input())):
    pricelist = [int(a) for a in input().split()]
    sample = (sorted(input()))
    amount=0
    for x in alpha:
        if x not in sample:
            amount += pricelist[alpha.index(x)]
            
    print(amount)
