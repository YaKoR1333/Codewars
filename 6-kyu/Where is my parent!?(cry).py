def find_children(s: str) -> str:
    return ''.join([(message + message.lower()*s.count(message.lower())) for message in sorted(s) if message.isupper()])
