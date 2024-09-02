def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid_move(board, row, col, num):
    # this checks the row
    if num in board[row]:
        return False
    
    # this checks the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # this checks 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def get_valid_numbers(board, row, col):
    valid_numbers = []
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            valid_numbers.append(num)
    return valid_numbers

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    
    if row is None:
        return True  # Puzzle is solved
    
    valid_numbers = get_valid_numbers(board, row, col)
    
    for num in valid_numbers:
        board[row][col] = num
        
        if solve_sudoku(board):
            return True  # solution found
        
        board[row][col] = 0  # Backtrack
    
    return False  # solution not found

def print_board(board):
    for row in board:
        print(row)

board = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
]

if solve_sudoku(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
