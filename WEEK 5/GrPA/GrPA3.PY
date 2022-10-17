def distance(word_1, word_2):
    """
    compute distance between two words

    Arguments:
        word_1, word_2: strings
    Return:
        word_distance: int
    """
    if len(word_1) != len(word_2):
        return -1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    size = len(word_1)
    dist = 0
    for i in range(size):
        c1, c2 = word_1[i], word_2[i]
        d = abs(letters.index(c1) - letters.index(c2))
        dist += d
    return dist
