def validMountainArray(arr) -> bool:
    peak = max(arr)
    peak_idx = arr.index(peak)
    incresing_list = arr[:peak_idx + 1]
    decreasing_list = arr[peak_idx:]

    for i in range(len(incresing_list) - 1):
        if incresing_list[i] >= incresing_list[i + 1]:
            return False

    for j in range(len(decreasing_list) - 1):
        if decreasing_list[i] <= decreasing_list[i + 1]:
            return False

    return True

print(validMountainArray([0,3,2,1]))
print(validMountainArray([3,5,5]))
