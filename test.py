# x = 0
# loop = True
# while loop:
#     print("Huy")
#     x += 1
#     if x == 3:
#         break
#         print("huy")

# list = [4,5,1,8,9,10,5,6,4,3]
# print (list[0:3])
# print (list[-3:])

# list.sort()
# print(list)

# list.sort(reverse = True)
# print(list)

arr = [4,5,1,8,9,10,5,6,4,3] 

def bubbleSort(arr): 
    n = len(arr)
    huy = True 
    while huy: 
        huy = False
        for j in range(n-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                huy = True
    

    # n = len(arr) 
    # for i in range(n-1): 
    #     for j in range(0, n-i-1): 
    #         if arr[j] < arr[j+1] : 
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)
print(arr)



# def bubbleSort(array):
#     n = len(array)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(n - 1):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#                 swapped = True
#         n -= 1
#     return array


# def main():
#     array = [1, 7, 4, 3, 2, 9, 8, 5, 6]
#     array = bubbleSort(array)
#     print(array)


# if __name__ == '__main__':
#     main()


