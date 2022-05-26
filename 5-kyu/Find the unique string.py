def find_uniq(arr):
    for index, string in enumerate(arr):
        if set(string.lower()) != set(arr[-len(arr)+index+1].lower()) and \
                set(string.lower()) != set(arr[-len(arr)+index+2].lower()):
            return string
