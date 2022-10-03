for _ in range(int(input())):

    x = int(input().split()[1])
    string = [*(input())]
    move = [x]

    for i in string:
        
        if i == 'R':
            x += 1
            move.append(x)
        elif i == 'L':
            x -= 1
            move.append(x)  
    print(len([*set(move)]))
