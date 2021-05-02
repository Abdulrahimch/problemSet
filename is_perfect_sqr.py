def is_perfect_square(num):
    lo, hi = 1, num
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if mid * mid == num:
            return True
        elif mid * mid > num:
            hi = mid - 1
        else:
            lo = mid + 1
    return False

print(is_perfect_square(1024))