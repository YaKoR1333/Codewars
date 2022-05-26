def scramble(s1, s2):
    for symbol in set(s2):
        if s1.count(symbol) < s2.count(symbol):
            return False
    return True
