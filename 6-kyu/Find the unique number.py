from collections import Counter


def find_uniq(arr: list):
    return Counter(arr).most_common(2)[1][0]
