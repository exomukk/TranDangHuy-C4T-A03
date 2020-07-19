n = int(input())

def hanoi_tower_recursion(n):
    if n == 1:
        result = 1
    else:
        result = 2*(hanoi_tower_recursion(n-1)) + 1
    return result

print(result)