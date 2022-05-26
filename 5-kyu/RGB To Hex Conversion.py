def rgb(r, g, b):
    list_rgb = [r, g, b]
    correct_list_rgb = ''
    for i in list_rgb:
        if i > 255:
            correct_list_rgb += str(hex(255)[2:].upper())
        elif i < 0:
            correct_list_rgb += str('0'+hex(0)[2:].upper())
        elif i <= 9:
            correct_list_rgb += str('0'+hex(i)[2:].upper())
        else:
            correct_list_rgb += str(hex(i)[2:].upper())
    return correct_list_rgb
