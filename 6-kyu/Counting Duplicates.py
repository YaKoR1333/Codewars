def duplicate_count(text: str) -> int:
    return sum([text.lower().count(c) > 1 for c in set(text.lower())])
