def anagrams(word, words):
    NewAnagrams = []
    for i in words:
        AnnagramWord = ''
        for j in word:
            if len(word) != len(i):
                break
            elif word. count(j) == i. count(j):
                AnnagramWord += j
                continue
            else:
                break
        if len(AnnagramWord) == len(word):
            NewAnagrams.append(i)
    print(NewAnagrams)
    return NewAnagrams
