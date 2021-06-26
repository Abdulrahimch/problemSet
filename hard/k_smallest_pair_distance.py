def smallestDistancePair(nums,k):
    nums.sort()
    low = 0
    high = nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if is_smallest_pair(nums, k, mid):
            high = mid
        else:
            low = mid + 1
    return low

def is_smallest_pair(nums, k, mid):
    left = 0
    counter = 0
    for right in range(len(nums)):
        while (nums[right] - nums[left]) > mid:
            left += 1
        counter += right - left
    #     if counter >= k: return True
    # return False
    return counter >= k

print(smallestDistancePair([62,100,4],2))