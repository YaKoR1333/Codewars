def order_weight(strng):
    weight_list = sorted(strng.split())
    right_weight_list = sorted(weight_list, key=sum_weight_list)
    return ' '.join(right_weight_list)


def sum_weight_list (n):
    return sum([int(i) for i in n])
