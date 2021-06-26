# [1, 1, 4, 5, 6, 8, 55, 77, 90],  [1, 1, 5] ,[100, 150, 202, 400],
import heapq as heap
def kSmallestPairs(nums1, nums2 , k):
    result = []
    for i in nums1[:k]:
        for j in nums2[:k]:
            result.append([i+j, i, j])
    k_sallest = heap.nsmallest(k, result)
    k_sallest = [i[1:] for i in k_sallest]
    return k_sallest





print(kSmallestPairs([100, 150, 202, 400],[1, 2, 4, 5, 6, 8, 55, 77, 90], 4))
print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))