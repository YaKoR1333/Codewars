def move_zeros(array):
    fil_list = list(filter(lambda x: x != 0, array))
    for i in range(len(array)-len(fil_list)):
        fil_list.append(0)
    return fil_list
