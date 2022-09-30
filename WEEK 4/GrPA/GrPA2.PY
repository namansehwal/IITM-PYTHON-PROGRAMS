def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    for i in range(len(marks)):
        for j in range(len(marks)-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    if len(marks)%2 == 0:
        median = (marks[len(marks)//2] + marks[len(marks)//2 - 1])/2
    else:
        median = marks[len(marks)//2]

    ### Enter your solution above this line
    return median