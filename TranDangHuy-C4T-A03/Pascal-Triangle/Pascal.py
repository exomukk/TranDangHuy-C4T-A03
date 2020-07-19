def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        row = [1]
        result = pascal(n-1)
        row2 = result[-1]
        for i in range(len(row2)-1):
            row.append(row2[i] + row2[i+1])
        row += [1]
        result.append(row)
    return result[-1]
x = pascal(5)   
print(x)