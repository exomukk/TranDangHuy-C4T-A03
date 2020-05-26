length = int(input("Input length: "))
width = int(input("Input width: "))

listRectangle = []

whileLoop = True
i = 0

while whileLoop:
    square = 2**i
    if length >= square and width >= square:
        listRectangle.append(square)
        i += 1
    else:
        whileLoop = False

amout = 0

for j in range(len(listRectangle)-1,-1,-1):
    num = listRectangle[j]
    a1 = length // num
    a2 = width // num
    a3 = a1 * a2 - amout * 4
    amout = a1 * a2
    print(a3,"-",num,"x",num)

#Anh check code nay voi neu duoc anh giup em ktra may cai trong Function def voi...k hieu sao no bao loi T-T
#Ah ca merge em cung chua lam duoc T-T con tam giac pascal thi anh bao k qtam nen thoi bo qua nhe :3
