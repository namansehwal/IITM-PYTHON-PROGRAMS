def get_marks(scores_dataset, subject):
    list = [ ]
    for student in scores_dataset:
        marks = student[subject]
        name = student['Name']
        list.append((name, marks))
    return list
