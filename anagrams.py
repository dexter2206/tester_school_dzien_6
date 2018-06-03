def are_anagrams(first, second):

    hist_first = {}
    hist_second = {}

    for char in first:
        hist_first[char] = hist_first.get(char, 0) + 1

    for char in second:
        hist_second[char] = hist_second.get(char, 0) + 1

    return hist_first == hist_second