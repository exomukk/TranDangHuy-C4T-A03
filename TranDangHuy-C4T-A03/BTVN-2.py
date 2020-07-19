huy1 = [1,3,4,16,32,8,64,4,128,2,256,32]

for i in range(len(huy1)):
    num1 = huy1[i]
    huy1[i]=0
    for j in range(len(huy1)):
        num2 = huy1[j]
        if num1*num2 == 256:
            huy1[j]=0
            print(num1,"",num2, "- vị trí:",i+1,"-",j+1)
            num1 = num2 = 0

# huy2 = [12,2,4,2,128,64,16,7,1,64,32,16,5,8]

# for i in range(len(huy1)):
#     num1 = huy2[i]
#     huy2[i]=0
#     for j in range(len(huy2)):
#         num2 = huy2[j]
#         if num1*num2 == 256:
#             huy2[j]=0
#             print(num1,"",num2, "vị trí:",i+1,"-",j+1)
#             num1 = num2 = 0

# Thử với list thứ 2 thì anh bỏ # đi nhé :3 