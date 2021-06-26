def sortedArrayToBST(nums):
    mid = len(nums) // 2

    left_nums = nums[:mid]
    right_nums = nums[mid + 1:]
    print('left_nums : ', left_nums)
    print('right_nums: ', right_nums)
    left_nums.reverse()
    right_nums.reverse()
    nums[0] = nums[mid]
    nums[1] = left_nums[0]
    nums[2] = right_nums[0]
    print('nums is: ', nums)
    left_pointer = 1
    right_pointer = 2


    for i in range(1, len(left_nums)):
        left_pointer = left_pointer * 2 + 1
        nums[left_pointer] = left_nums[i]
        nums[left_pointer + 1] = 'null'

    for i in range(1, len(right_nums)-1):
        right_pointer = right_pointer * 2 + 1
        nums[right_pointer] = right_nums[i]
        nums[right_pointer + 1] = 'null'

    return nums
print(sortedArrayToBST([1,2,3,4,5]))