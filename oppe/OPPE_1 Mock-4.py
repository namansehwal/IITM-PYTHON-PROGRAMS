def exact_count(para, n):
    para = para.split(' ')
    for element in para:
        if para.count(element) == n:
            return True
    return False        

