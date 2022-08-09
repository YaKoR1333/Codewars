def is_valid_walk(walk: list[str]) -> bool:
    starting_point = [0, 0]
    for way in walk:
        if way == 's':
            starting_point[0] += 1
        elif way == 'n':
            starting_point[0] -= 1
        elif way == 'e':
            starting_point[1] += 1
        elif way == 'w':
            starting_point[1] -= 1
    return starting_point == [0, 0] and len(walk) == 10
