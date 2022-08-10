def narcissistic(value: int) -> bool:
    return value == sum(list(map(lambda x: int(x) ** len(str(value)), str(value))))
