# def partition(A, pivot):
#     items_left = []
#     items_right = []
    
#     for item in A:
#         if item < pivot:
#             items_left.append( item )
#         else:
#             items_right.append( item )
    
#     A = items_left + items_right
#     return A

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)

array = [5,3,4,2,6,9,7,8]
quick_sort(array, 0, len(array) - 1)
print(array)


    