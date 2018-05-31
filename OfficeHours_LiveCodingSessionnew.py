# The sudoku app

# Steps for solving problems:
#
# 1) Understand Problem
#        - What are the inputs -> list of lists
#        - What are the outputs -> True or False
#
# 2) Plan a solution
#       - You can do this on paper!
#       - Or with "pretend" code <- we're using this one
#
# 3) Fill out your solution!
#       - Test along the way!

DESIRED_SUM = 1+2+3+4+5+6+7+8+9

INVALID_GRID = [[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]]

VALID_GRID = [[4,3,5,2,6,9,7,8,1],
               [6,8,2,5,7,1,4,9,3],
               [1,9,7,8,3,4,5,6,2],
               [8,2,6,1,9,5,3,4,7],
               [3,7,4,6,8,2,9,1,5],
               [9,5,1,7,4,3,6,2,8],
               [5,1,9,3,2,6,8,7,4],
               [2,4,8,9,5,7,1,3,6],
               [7,6,3,4,1,8,2,5,9]]


def check_sudoku(sudoku_grid):
    # Want this function to return True when the solution is correct
    if check_rows(sudoku_grid) == True:
        print "rows look good"
        if check_columns(sudoku_grid) == True:
            print "columns look good"
            if check_squares(sudoku_grid) == True:
                return True

def check_rows(grid):
    for row in grid:
        if is_valid_row(row) == False:
            return False
    return True

def is_valid_row(row):
    required_numbers = [1,2,3,4,5,6,7,8,9]
    for number in required_numbers:
        if number not in row:
            return False
        return True

def check_columns(grid):
    columns = []
    for index in range(9):
        new_column = []
        for row in grid:
            new_column.append(row[index])
        columns.append(new_column)
    return check_rows(columns)

def check_squares(grid_9by9):
    rows_of_squares = make_squares(grid_9by9)
    for rows_of_squaresin rows_of_squares:
        for square in rows_of_squares:
            if check_square(square) == False:
                return False
    return True

#print check_rows(VALID_GRID)
#print check_columns(INVALID_GRID)
#print check_sudoku(VALID_GRID)
