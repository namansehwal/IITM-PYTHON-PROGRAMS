sample = int(input())
result = list()
for length in range(1,sample//2):
    for width in range(1,sample+1):
        if length*width == sample and width not in result and length not in result:
            result.append(length)
            result.append(width)
            print(f'{length},{width}')
            break
       