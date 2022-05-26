import string

def is_pangram(s):
    ns = s.lower()
    for i in string.printable[10:36]:
        if i in ns:
            continue
        else:
            return False
    return True
