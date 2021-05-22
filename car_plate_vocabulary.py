
def find_shortest_word(plate, vocabulary):
    v = "".join([i for i in plate.strip() if i.isalpha()])
    place_holder=''
    ##convert to lowercase
    v = v.lower()
    vocab_lower = [i.lower() for i in vocabulary]
    if v not in vocab_lower:
        place_holder=""
        
    if len(vocab_lower)== 0:
        place_holder=''
        
    ##create a vocabulary letter number mapping
    vocab_keys=[chr(i) for i in range(97,123)]
    vocab_values=[i for i in range(97,123)]
    ##creating the vocabulary dictionary
    vocab_map = dict(zip(vocab_keys,vocab_values))

    # return "".join([i for i in vocab_lower if set(i)-set(v)==0])
    for i in vocab_lower:
        if len(set(i) - set(v)) == 0 or len(set(i) - set(v)) == 1:place_holder=i
        if set(i) == set(v):return i
    return place_holder


print(find_shortest_word("RT 123 SO", ["sort", "car", "rest", "rust", "sir", "cast"]))#SORT