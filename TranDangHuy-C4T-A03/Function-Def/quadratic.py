import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def quadratic_math(a, b, c):
    if (a == 0):
        print ("Phuong trinh khong phai la phuong trinh bac 2")
    
    delta = b * b - 4 * a * c
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))//2
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))//2
        print ("Phuong trinh co 2 nghiem: x1 = ", x1, " - x2 = ", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("Phuong trinh co nghiem kep: x1 = x2 = ", x1)
    else:
        print("Phuong trinh vo nghiem")

quadratic_math(a, b, c)