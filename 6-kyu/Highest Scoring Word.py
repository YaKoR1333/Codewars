def high(x):
    word_list = x.split()
    score_list = []
    for word in word_list:
        score = 0
        i = 0
        for counter, symbol in enumerate(range(97, 123), start=1):
            if i > len(word)-1:
                break
            elif word.count(chr(symbol)) >= 1:
                score += counter * word.count(chr(symbol))
                i += 1
            else:
                continue
        score_list.append(score)
    return word_list[(score_list.index(max(score_list)))]
