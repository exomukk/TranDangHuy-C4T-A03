def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    return n % 2,end = ''
    

num = 13
convertToBinary(num)
print(convertToBinary)