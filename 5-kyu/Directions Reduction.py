def dirReduc(arr):
    directions = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for i in arr:
        if res and directions[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res
