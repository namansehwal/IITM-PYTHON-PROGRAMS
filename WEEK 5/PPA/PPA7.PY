def is_empty(l):
    if len(l)==0:
        return True
    else:
        return False
def first(l):
    if not is_empty(l):
        return l[0]
    else:
        return 'None'
def last(l):
    if not is_empty(l):
        return l[-1]
    else:
        return 'None'
def init(l):
    if not is_empty(l):
        return l[:-1]
    else:
        return 'None'
def rest(l):
    if not is_empty(l):
        return l[1:]
    else:
        return 'None'