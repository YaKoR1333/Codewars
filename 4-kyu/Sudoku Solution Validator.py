def row_and_column(board):
    sudoku_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotated_board = tuple(zip(*board[::-1]))
    for line in zip(board, rotated_board):
        if sorted(line[0]) == sorted(line[1]) == sudoku_number:
            continue
        else:
            return False
    return True


def cube(board):
    sudoku_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cube_sudoku_1 = []
    cube_sudoku_2 = []
    cube_sudoku_3 = []
    for index, line in enumerate(board, start=1):
        cube_sudoku_1 += line[:3]
        cube_sudoku_2 += line[3:6]
        cube_sudoku_3 += line[6:]
        if index % 3 == 0:
            if sorted(cube_sudoku_1) == sorted(cube_sudoku_2) == sorted(cube_sudoku_3) == sudoku_number:
                cube_sudoku_1 = []
                cube_sudoku_2 = []
                cube_sudoku_3 = []
                continue
            else:
                return False
    return True


def valid_solution(board):
    return row_and_column(board) and cube(board)
