def string_process(S1,S2):
    min = 0
    max = 0
    for i in range(len(S1)):
        if S1[i] != S2[i] and S1[i] != '?' and S2[i] != '?':
             min += 1
             max += 1
        elif S1[i] == '?' and S2[i] == '?':
             max += 1
        elif S1[i] == '?' or S2[i] == '?':
             max += 1
             
    return min,max    


for _ in range(int(input())):

   S1 = input()
   S2 = input()
   print(*string_process(S1,S2))
   
    


