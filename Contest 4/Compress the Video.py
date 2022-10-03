def compress_the_video(video):
    
    result = []
    temp = int()
    
    for i,e in enumerate(video):
        if temp!=e:
            result.append(e)
            temp=e
            
    return len(result)

for _ in range(int(input())):
    no_need = input()
    
    numlist = [int(a) for a in input().split()]

    print(compress_the_video(numlist))  

