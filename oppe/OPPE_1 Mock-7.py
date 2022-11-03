def mentors(scores_dataset, subject):
    temp_dict={}
    for dataset in scores_dataset:
        temp_dict[dataset['SeqNo']]=[]
        temp_marks=dataset[subject]
        for i in scores_dataset:
            c=temp_marks-i[subject]
            if c>=10 and c<=20:
                temp_dict[dataset['SeqNo']].append(i['SeqNo'])
    return temp_dict
