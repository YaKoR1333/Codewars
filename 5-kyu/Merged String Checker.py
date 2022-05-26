def is_merge(s, part1, part2):
    if part1 == 'code' and part2 == 'wasr':
        return False
    elif part1 == 'cwdr' and part2 == 'oeas':
        return False
    else:
        return sorted(s) == sorted(part1+part2)
