# length = int(input("Input length: "))
# width = int(input("Input width: "))

# listRectangle = []

# whileLoop = True
# i = 0

# while whileLoop:
#     square = 2**i
#     if length >= square and width >= square:
#         listRectangle.append(square)
#         i += 1
#     else:
#         whileLoop = False

# amout = 0

# for j in range(len(listRectangle)-1,-1,-1):
#     num = listRectangle[j]
#     a1 = length // num
#     a2 = width // num
#     a3 = a1 * a2 - amout * 4
#     amout = a1 * a2
#     print(a3,"-",num,"x",num)


def minTile(n,m):
    if n == 0 or m == 0:
        return 0
    
    elif n % 2 == 0 and m % 2 == 0:
        return minTile(int(n/2), int(m/2))

    elif n % 2 == 0 and m % 2 == 1:
        return (n + minTile(int(n/2), int(m/2)))
    
    elif n % 2 == 1 and m % 2 == 0:
        return (m + minTile(int(n/2), int(m/2)))

    else:
        return (n + m - 1 + minTile(int(n/2), int(m/2)))


print (minTile(5,6))

