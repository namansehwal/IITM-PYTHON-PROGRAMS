def get_toppers(scores_dataset, subject, gender):
    """
    Get the toppers in subject belonging to gender

    Arguments:
        scores_dataset: list of dicts
        subject: string
        gender: string ('F' or 'M')
    Return:
        list of strings
    """
    output = []
    max_marks = float('-inf')
    for score in scores_dataset:
        if score['Gender'] == gender:
            if max_marks == score[subject]:
                output.append(score['Name'])
            elif max_marks < score[subject]:
                output = [score['Name']]
                max_marks = score[subject]
    
    return output