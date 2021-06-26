# [4,3,2,1,1,2,3,1]
def minimumMountainRemovals(nums):
    max_val = max(nums)
    max_val_idx = nums.index(max_val)
    increasing_arr = nums[:max_val_idx + 1]
    decreasing_arr = nums[max_val_idx:]
    i, j = 0, 0
    while i < len(increasing_arr) - 2:
        if increasing_arr[i] >= increasing_arr[i + 1]:
            increasing_arr.pop(i)
            i -= 1
        i += 1

    while j < len(decreasing_arr) - 2:
        if decreasing_arr[j] <= decreasing_arr[j + 1]:
            decreasing_arr.pop(j)
            j -= 1
        j += 1
    nums = increasing_arr[:-1] + decreasing_arr
    return nums

def is_mountain_arr(arr) -> bool:
    peak = max(arr)
    peak_idx = arr.index(peak)
    incresing_list = arr[:peak_idx+1]
    decreasing_list = arr[peak_idx:]

    if len(incresing_list) <= 1 or len(decreasing_list) <= 1:
        return False

    for i in range(len(incresing_list) - 1):
        if incresing_list[i] >= incresing_list[i + 1]:
            return False

    for j in range(len(decreasing_list) - 1):
        if decreasing_list[j] <= decreasing_list[j + 1]:
            return False

    return True

def last_result(nums):
    if is_mountain_arr(nums):
        return 0
    # result = minimumMountainRemovals(nums)
    # counter = 0
    # print('result is: ', result)
    # while result == 0:
    #     counter += 1
    #     nums.pop(nums.index(max(nums)))
    #     result = minimumMountainRemovals(nums)
    len_nums = len(nums)
    while max(nums) == nums[0]:
        nums = nums[1:]
    while not is_mountain_arr(nums):
        nums = minimumMountainRemovals(nums)
    return len_nums - len(nums)

print(last_result([4,3,2,1,1,2,3,1]))
print(last_result([2,1,1,5,6,2,3,1]))
print(last_result([4,3,2,1,1,2,3,1]))
print(last_result([2,1,1,2,3,1]))
print(last_result([1,16,84,9,29,71,86,79,72,12]))
print(last_result([2,1,1,5,6,2,3,1]))
print(last_result([2,9,19,45,41,96,72,40,100,37,36,13,7]))

