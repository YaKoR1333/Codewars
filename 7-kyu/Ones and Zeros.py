def binary_array_to_number(arr):
    string = ''
    for i in arr:
        string += str(i)
    return int(string, 2)
