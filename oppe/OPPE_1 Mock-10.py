area = int(input())
result = list()
for length in range(1,area):
    for width in range(1,area+1):
        
        if length*width == area and width not in result and length not in result:
            result.append(length)
            result.append(width)
            print(f'{length},{width}')
            break
       