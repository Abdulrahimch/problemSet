# matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
import heapq as heap
def kthSmallest(matrix, k):
    j = matrix[0]
    for li in matrix[1:]:
        j.extend(li)
    k_smallest_nums = heap.nsmallest(k, j)
    return k_smallest_nums[-1]



print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))