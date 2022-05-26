def solver (n, coins, i):
    if i < 0 or n < 0:
        return 0
    if n == 0:
        return 1
    count = solver(n, coins, i-1) + solver(n-coins[i], coins, i)
    return count


def count_change(money, coins):
    return solver(money, coins, len(coins) - 1)
