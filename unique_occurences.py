# Given an array of integers arr, write a function that returns true
# if and only if the number of occurrences of each value in the array is unique.

def unique_occurrences(arr):
    dic = {}
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.values():
        if list(dic.values()).count(i) > 1:
            return False
    return True

arr = [1,2,2,1,1,3]
print(unique_occurrences(arr))
