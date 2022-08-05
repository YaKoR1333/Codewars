def divisible_count(x: int, y: int, k: int) -> int:
    if x % k == 0:
        return ((y // k) - (x // k)) + 1
    return (y // k) - (x // k)
