def binarySearch(nums, target):
    
    left = 0
    right = len(nums) -1


    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


nums = [-1,0,3,5,9,12]

print(binarySearch(nums, 12))