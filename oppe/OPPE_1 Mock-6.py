# def max_subject()

# def crowded_group(scores_dataset, subject, mark_limit):
#    max = 0
#    target_list= [0] * (mark_limit+1)
#    for element in range(len(scores_dataset)):
#         if scores_dataset[element]['Subject'] == subject:
#             target_list[scores_dataset[element]['Marks']] += 1
       
       
def crowded_group(scores_dataset, subject, mark_limit): 
    List1=[]
    for dataset in scores_dataset:
        temp_marks=dataset[subject]
        higher_temp_marks=temp_marks+mark_limit
        group=0
        for dataset in scores_dataset:
            if abs(dataset[subject])>=temp_marks and abs(dataset[subject])<=higher_temp_marks:
                group+=1
        List1.append(group)
    return max(List1)    