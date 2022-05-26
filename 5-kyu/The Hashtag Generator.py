def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    word = s.strip().split()
    return '#'+''.join(map(lambda x: str(x).capitalize(), word))
