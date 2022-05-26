def solution(args):
    correct_range = ''
    counter_range = 0
    end_range = 0
    begin_range = 0
    for index, number in enumerate(args, start=0):
        if (args[-len(args)+1+index] - args[-len(args)+index]) == 1:
            counter_range += 1
            if counter_range == 1:
                begin_range = number
                if (args[-len(args)+2+index] - args[-len(args)+1+index]) != 1:
                    correct_range += str(number) + ','
            elif counter_range >= 2:
                end_range = number + 1
        elif counter_range >= 2:
            correct_range += str(begin_range) + '-' + str(end_range) + ','
            counter_range = 0
        else:
            counter_range = 0
            correct_range += str(number) + ','
    return correct_range[:-1]
