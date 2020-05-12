# nhapso = int(input("Nhap so bat ky de kiem tra so nguyen to: "))
# for j in range (1, 10):
#     if nhapso > 1:
#         for i in range (1,nhapso):
        
#             if (nhapso % i) == 0 and (nhapso % j) == 0 and nhapso == j:
#                 print(nhapso, "1-khong la so nguyen to!")
                
#             else:
#                 print(nhapso, "2- la so nguyen to!")
#                 break

#     else:
#         print(nhapso, "3-khong phai la so nguyen to!")
#     break

# Em lười xóa phần trên quá... thôi giữ làm kỷ niệm anh nhé :3

huy = int(input("Nhap 1 so bat ky: "))  
  
if huy > 1:  
   for i in range(2,huy):  
       if (huy % i) == 0:  
           print(huy,"khong la so nguyen to!")  
           break  
   else:  
       print(huy,"la so nguyen to")  
         
else:  
   print(huy,"khong la so nguyen to")  
