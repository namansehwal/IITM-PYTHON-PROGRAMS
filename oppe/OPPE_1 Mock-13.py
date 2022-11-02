
# def most_freq(M):
#     parent = list()
#     for x in M:
#         for y in x:
#             parent.append(y)

    
#     max_count = 0
#     maximum = 0
#     for x in parent:
#         if parent.count(x) >= max_count:
#             max_count = parent.count(x)
#             maximum = max(x, maximum)
           

#     print(maximum)    
# most_freq([[2, 8, 2, 3], [8, 7, 2, 8], [8, 3, 2, 3]])    


def most_freq(M):
    parent = list()
    for x in M:
         parent.extend(x)
    unique = list(reversed(sorted(list(set(parent)))))
    y  = max(parent.count(x) for x in unique)
    for x in unique:
        if parent.count(x) == y:
            return x
    # for element in unique:
    #     if parent.count(element) == max(parent.count(x) for x in unique):
    #         return element 
    
most_freq([[2, 8, 2, 3], [8, 7, 2, 8], [8, 3, 2, 3]])       