def two_level_sort(scores):
    """
    Perform a two-level sort

    Argument: 
        scores: list of tuples, (string, integer)
    Return:
        result: list of tuples (string, integer)
    """
    dict_ = {}
    score_list = []
    for i in scores:
        if(i[1] in dict_):
            dict_[i[1]].append(i[0])
        else:
            dict_[i[1]] = [i[0]]
            score_list.append(i[1])
    score_list.sort()
    d_level1_sort = {}
    for i in score_list:
        d_level1_sort[i] = dict_[i]
        d_level1_sort[i].sort()
    final=[]
    for i in score_list:
        for j in d_level1_sort[i]:
            x=(j,i)
            final.append(x)
    return final