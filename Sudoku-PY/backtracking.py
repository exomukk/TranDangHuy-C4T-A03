board = [
    [7, 8, 3, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, [row, col]):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)

    return None

def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]] == num and pos[1] != i:  #Hang
            return False

    for i in range(len(bo)):
        if bo[pos[1]] == num and pos[0] != i:   #Cot
            return False

    box_R = pos[1] // 3         #Hinh vuong
    box_C = pos[0] // 3
    for i in range(box_C*3, box_C*3 + 3):
        for j in range(box_R*3, box_R*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)
solve(board)
print("")
print ("Solved:")
print_board(board)

    