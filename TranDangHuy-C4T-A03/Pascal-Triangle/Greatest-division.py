# def greatest_division(x, y):  
#     if x > y: 
#         num = y 
#     else: 
#         num = x 
#     for i in range(1, num+1): 
#         if((x % i == 0) and (y % i == 0)): 
#             gd = i           
#     return gd 

# print (greatest_division(20,16)) 

def greatest_division(a,b): 
    if a == b: 
        return a
    elif a>b:
        return greatest_division(b,a-b)     
    else: 
        return greatest_division(a,b-a) 

print (greatest_division(9,3)) 