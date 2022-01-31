def get_n_longest_unique_words(words, n):
    uni_words = []
    for word in words:
        if words.count(word) == 1:
            uni_words.append(word)
    sorted_words = sorted(uni_words, key=len, reverse=True)
    return(sorted_words[:n])
