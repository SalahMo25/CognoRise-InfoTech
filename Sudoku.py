def solve_sudoku(sudoku):
    
    # check about an empty position => 0
    empty = empty_positions(sudoku)
    if not empty:
        return True  
    row, col = empty

    # here we will place the empty position with 1 to 9 nums
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num 

            if solve_sudoku(sudoku):
                return True
            
            #the incorrect num will be replaced to 0
            sudoku[row][col] = 0

    return False

# check if num is already correct or not
def is_valid(sudoku, row, col, num):
    #at row
    for r in range(9):
        if sudoku[row][r] == num:
            return False

    #at column
    for c in range(9):
        if sudoku[c][col] == num:
            return False

    # Check the 3x3 matrix
    row, col = 3 * (row // 3), 3 * (col // 3)
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if sudoku[i][j] == num:
                return False

    return True


def empty_positions(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return (row, col)
    return None


def result(sudoku):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("=" * 21)  
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            print(sudoku[row][col], end=" ")
        print()


sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


if solve_sudoku(sudoku):
    result(sudoku)
else:
    print("Try to solve another sudoku")
