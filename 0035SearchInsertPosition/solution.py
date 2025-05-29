def searchRange(nums, target: int):



    return [FindFirst(nums,target), FindLast(nums,target)]




def FindFirst(nums, target):
    left = 0
    right = len(nums) - 1
    first = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            first = mid     
            right = mid - 1       
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return first


def FindLast(nums, target):
    left = 0
    right = len(nums) - 1
    last = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            last = mid     
            left = mid + 1       
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return last

print(searchRange([5,7,7,8,8,10], 8))
