iter_brackets = iter('(){}[]')
dict_parens = dict(zip(iter_brackets, iter_brackets))
closing = dict_parens.values()


def valid_braces(string: str) -> bool:
    stack = []
    for c in string:
        d = dict_parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack
