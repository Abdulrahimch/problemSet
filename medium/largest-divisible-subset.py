# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def largestDivisibleSubset(nums):
    if not nums: return []
    nums.sort()
    dp = [set() for _ in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0 :
                if 1 + len(dp[j]) > len(dp[i]):
                    dp[i] = dp[j] | {nums[i]}
                    print('after ', i, j, dp)

        dp[i] |= {nums[i]}
    print(dp)
    return max(dp, key=len)
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
