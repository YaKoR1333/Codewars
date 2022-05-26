def valid_ISBN10(isbn):
    sum_number = 0
    if len(isbn) != 10:
        return False
    for index, number in enumerate(isbn, start=1):
        if number == 'X' and isbn[-1] == 'X' and index == len(isbn):
            number = 10
        try:
            sum_number += int(number) * index
        except ValueError:
            return False
    if sum_number % 11 == 0:
        return True
    else:
        return False
