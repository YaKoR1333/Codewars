from collections import Counter


def permute_a_palindrome(mystring: str) -> bool:
    alpha_chars_only = [x for x in mystring.lower() if x.isalpha()]
    counts = Counter(alpha_chars_only)
    number_of_odd = sum(1 for letter, cnt in counts.items() if cnt%2)
    return number_of_odd <= 1
