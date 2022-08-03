def perimeter(n: int) -> int:
    fib1 = fib2 = 1
    sum_number = 0
    while (n-1) > 0:
        fib1, fib2 = fib2, fib1 + fib2
        sum_number += fib2
        n -= 1
    return sum_number * 4 + 8
