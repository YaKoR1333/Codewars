def electrons_around_the_cores(dice):
    sum_number = 0
    number_value = {1: 0,
                    2: 0,
                    3: 2,
                    4: 0,
                    5: 4,
                    6: 0, }
    return sum(list(map(lambda x: sum_number + number_value.get(x), dice)))
