import math
def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions



    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    
    
    for i in range(len(l)//2):
        l[i], l[-i-1] = l[-i-1], l[i]
    return l



def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.



    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.



    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    missing_possition = find_missing_number(matrix)
    if missing_possition == None:
        return True
    row, col = missing_possition
    for num in range(1,len(matrix)+1):
        if check_correctness(matrix,row,col,num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0

def find_missing_number(matrix):

    '''
    ### find out the missing number from the matrix
    :param matrix: List[List[integer]](n*n)list of integers
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i, j
    return None

def check_correctness(matrix,row,col,num):

    '''
    ### check the correctness of the matrix when a number is placed at a particular position
    :param matrix: List[List[integer]](n*n)list of integers
    :param row: integer the row position where the number is placed
    :param col: integer the column position where the number is placed
    :param num: integer number to be placed at a particular position
    '''
    
    # check row and column
    for i in range(len(matrix)):
        if matrix[row][i] == num or matrix[i][col] == num:
            return False
    
    # check subgrid
    index = int(math.sqrt(len(matrix)))
    start_row = row - row%index
    start_col = col - col%index
    for i in range(start_row, start_row+index):
        for j in range(start_col, start_col+index):
            if matrix[i][j] == num:
                return False
    return True

if __name__ == "__main__":
    # Test case 1
    print("Test case 1")
    l = [1, 2, 3, 4, 5]
    print(reverse_list(l)) # [5, 4, 3, 2, 1]
    # Test case 2
    print("Test case 2")
    m = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solve_sudoku(m)
    for row in m:
        print(' '.join(str(num) for num in row))