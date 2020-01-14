# function that uses recursion to solve the board
def solve_board(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve_board(bo):
                return True

            bo[row][col] = ""

    return False

# check is the given number is valid in the given position on the given board
def valid(bo, num, pos):
    # Checks row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checks column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks box
    x_box = pos[1] // 3
    y_box = pos[0] // 3

    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# finds empty squares in the board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == "":
                return (i, j)  # row, col

    return None



# checks to see if the given board is valid
def valid_board(bo):
    bo = int_board(bo)
    # Checks row
    for i in range(len(bo)):
        row_list = []
        for j in range(9):
            if bo[i][j] != "":
                row_list.append(bo[i][j])
        row_set = set()
        for elem in row_list:
            if elem in row_set:
                return False
            else:
                row_set.add(elem)

    # Checks column
    for i in range(9):
        col_list = []
        for j in range(9):
            if bo[j][i] != "":
                col_list.append(bo[j][i])
        col_set = set()
        for elem in col_list:
            if elem in col_set:
                return False
            else:
                col_set.add(elem)

    # Checks boxes
    boxes = [{} for i in range(9)]
    for i in range(9):
        for j in range(9):
            if bo[i][j] != "":
                box_ind = (i//3 * 3 + j//3)

                boxes[box_ind][bo[i][j]] = boxes[box_ind].get(bo[i][j], 0) + 1
                if boxes[box_ind][bo[i][j]] > 1:
                    return False

    return True

# makes the board integers in case they are not
def int_board(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] != "":
                bo[i][j] = int(bo[i][j])

    return bo
