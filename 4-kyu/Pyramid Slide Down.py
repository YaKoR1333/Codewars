def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    last_string = pyramid[-1]
    add_string = []
    for i in range(1, len(last_string)):
        add_string.append(max(last_string[i], last_string[i - 1]))
    pyramid[-2] = [a + b for a, b in zip(pyramid[-2], add_string)]
    return longest_slide_down(pyramid[:-1])
