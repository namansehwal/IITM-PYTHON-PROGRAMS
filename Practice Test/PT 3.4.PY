question_marks=int(input())
choices=int(input())
correct_choices=input()
chosen_ch=input()
marks=0.0
c=len(correct_choices)//2+1
marks_per_ques=question_marks/c
for i in range(0, len(chosen_ch), 2):
    if chosen_ch[i] in correct_choices:
        marks=marks+marks_per_ques
    else:
        marks=0.0
        break
print(marks)


