def intersect(str1, str2):
    # [1,2,3,4,5] #[5,2,3,4,99]
    result = []
    for i in str1:
        if i in str2:
            result.append(i)
            str2.remove(i)
    return result

print(intersect([1,2,3,4,5], [5,2,3,4,99]))
