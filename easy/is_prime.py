import math
def is_prime(self, n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True