def merge(left, right):
    pass
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    
   
    left = right = 0
    list_merged = []  
    list_len_target = len(left) + len(right)
    while len(list_merged) < list_len_target:
        if left[index_left] <= right[index_right]:
            list_merged.append(left[index_left])
            index_left += 1
        else:
            list_merged.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            
            list_merged += left[index_left:]
            break
        elif index_left == len(left):
            
            list_merged += right[index_right:]
            break
        
    return list_merged

def mergeSort(nums):
    if len(nums) <= 1:
        return nums


    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_list = mergeSort(left)
    right_list = mergeSort(right)

    return merge(left_list, right_list)

    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         nums[k] = left[i]
    #         i += 1
    #     else:
    #         nums[k] = right[j]
    #         j += 1

    #     k += 1

    # while i < len(left):
    #     nums[k] = left[i]
    #     i += 1
    #     k += 1

    # while j < len(right):
    #     nums[k] = right[j]
    #     j += 1
    #     k += 1

nums = [1,5,8,9,2,4,10]
mergeSort(nums)
print(nums)
