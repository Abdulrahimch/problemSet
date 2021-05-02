# Merge Algo assumes that lists already sorted!

def merge(nums1, nums2):
    i = 0
    while i < len(nums1) and nums2 :
        if nums1[i] > nums2[0]:
            nums1.insert(i, nums2.pop(0))
        i += 1

    if nums2:
        nums1 += nums2
    return nums1

print(merge([15, 25, 35, 45, 55, 66, 456, 1024, 20000, 500000], [1, 2, 3, 10, 60, 70, 400, 150000]))