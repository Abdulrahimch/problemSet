def findKthLargest(nums, k):
    nums.sort(reverse=True)
    kth_largest = nums[k - 1]
    return kth_largest

