def solution(L):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    for i in range (len(L)):
        for j in range(i + 1, len(L)):
            if(L[i] < L[j]):
                t = L[i]
                L[i] = L[j]
                L[j] = t
        sorted_L=L
    ### Enter your solution above this line
    return sorted_L