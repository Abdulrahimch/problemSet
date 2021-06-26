def validMountainArray(arr) -> bool:
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
#
print(validMountainArray([0,3,2,1]))
print(validMountainArray([3,5,5]))
print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))
print(validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(validMountainArray([2,1]))

