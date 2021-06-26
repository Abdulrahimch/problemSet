# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# sorted_l = [2,3,4,5,6,10] target=9
# exp: [1,5,9,16,20,30]
def sum_two_digits(l, target):
    l.sort()
    left = 0
    right = len(l) -1
    while left < right:
        if l[left] + l[right] == target:
            return left, right

        if l[left] + l[right] > target:
            right -= 1
        else:
            left += 1
    return False


exp_ls = [4,5,9,6,3,1,2,4]
print(sum_two_digits(exp_ls, 10))