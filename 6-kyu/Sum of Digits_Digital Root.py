def digital_root(n: int) -> int:
    if len(str(n)) > 1:
        return digital_root(sum(list(map(lambda x: int(x), str(n)))))
    else:
        return n
