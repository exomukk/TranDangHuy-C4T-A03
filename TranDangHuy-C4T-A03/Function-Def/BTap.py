#Bai-1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(n))



#Bai-2

def getSum(n):  
    sum = 0
    while (n != 0): 
        sum = sum + int(n % 10) 
        n = int(n/10)   
    return sum

# print(getSum(5)) 


#Bai-3
def minimum_list (list):
    min = list [0]
    for a in list:
        if a < min:
            min = a
    return min

print(minimum_list([1,0,9,-8]))