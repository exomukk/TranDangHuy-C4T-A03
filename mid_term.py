#  Bài 1
#  def sum_of_digit(n):
#     if n == 0:
#         return 0
#     return (n % 10 + sum_of_digit(int(n / 10)))

# num = 1234
# result = sum_of_digit(num)
# print("Sum of digits in",num,"is", result)


# Bài 2
# def sum_num(n):
#    if n <= 1:
#        return n
#    else:
#        return n + sum_num(n-1)
# num = 4

# if num < 0:
#    print("Wrong number !")
# else:
#    print("The sum of",num,"number is",sum_num(num))


# Bài 3
# def decimalToBinary(n):
#     return bin(n).replace("0b", "")

# if __name__ == '__main__':
#     print(decimalToBinary(7))
#     print(decimalToBinary(10))


# Bài 4
# def maze_runner(maze):
#     maze[0][0] = "X"
#     if Solve_maze(maze, [0, 0]):
#         print_maze(maze)
#         return "Solved"
#     else:
#         return "Can't solve"


# def Solve_maze(maze, position):
#     x, y = position
#     if x == y and x == len(maze) - 1:
#         return True
#     next_move = find_next_move(maze, position)
#     for move in next_move:
#         next_x, next_y = move
#         current_value = maze[next_x][next_y]
#         maze[next_x][next_y] = "X"
#         if Solve_maze(maze, move):
#             return True
#         maze[next_x][next_y] = current_value
#     return False


# def find_next_move(maze, position):
#     side_length = len(maze)
#     valid_move = []
#     x, y = position
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         if 0 <= new_x < side_length and 0 <= new_y < side_length and maze[new_x][new_y] == 1:
#             valid_move.append([new_x, new_y])
#     return valid_move


# maze = [ [1, 0, 0, 0], 
#          [1, 1, 0, 1], 
#          [0, 1, 0, 0], 
#          [1, 1, 1, 1] ]


# def print_maze(maze):
#     for i in range(len(maze)):
#         for j in range(len(maze)):
#             print(maze[i][j], end=" ")
#         print()
#     print()

# print_maze(maze)
# print("Solved maze:")
# print(maze_runner(maze))


# Bài 5
# def possible_journey(start, destination):
#     sx, sy = start
#     dx, dy = destination
#     if sx == dx and sy == dy:
#         return True
    
#     if sx * sy > 0 and (abs(sx) > abs(dx) or abs(sy) > abs(dy)):
#         return False

#     if sx == sy or sx == 0:
#         return False

#     if sx == 0:
#         return possible_journey([sx + sy, sy],[dx, dy])

#     if sy == 0:
#         return possible_journey([sx, sx + sy],[dx,dy])

#     return possible_journey([sx + sy, sy],[dx, dy]) or possible_journey([sx, sx + sy],[dx,dy])

# print(possible_journey[sx,sy],[dx,dy])



# Bài 6
# import math

# def square_sum(x,n):
#     ways = 0
#     for i in range(1,x+1):
#         if pow(i,n) > x:
#             return ways
#         ways += square_sum_recursion(x - pow(i,n), n, i+1) 
#     return ways

# def square_sum_recursion(x,n,start):
#     if x == 0:
#         return 1
#     ways = 0
#     for i in range(start,x+1):
#         if pow(i,n) > x:
#             return ways
#         ways += square_sum_recursion(x - pow(i,n), n,i+1)
#     return ways

# for i in range(100):
#     ways = square_sum(i,2) 
#     if  ways > 3:
#         print("Number: {}, ways: {}".format(i,ways)) 



# Bài 7
def find_min_move(n):   
    if n == 0:              
        return 0
    n = abs(n)                  
    largest_min_move = find_min_move(n-1) + 2
    return find_min_move_recursion(n, 0, 1, largest_min_move)
    
def find_min_move_recursion(n, position, step, largest_min_move):
    if position == n:
        return step - 1
    if step >= largest_min_move:
        return largest_min_move
    else:
        return min( find_min_move_recursion(n, position + step, step + 1, largest_min_move), find_min_move_recursion(n, position - step, step + 1,largest_min_move) )

for i in range(1,21):
i = 12
print("{}. move: {}".format(i,find_min_move(i)))

