def freq_to_words(words):
    """
    Get the collection of all words that have a given frequency

    Argument
       words: list of strings
    Return: 
       result: dictionary 
           key: integer
           value: list of strings
    """
    output = {}
    for word in words:
        count = words.count(word)
        if count in output.keys():
            if word not in output[count]:
                output[count].append(word)
        else:
            output[count] = [word]
    
    return output
