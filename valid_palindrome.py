def is_palindrome(s: str) -> bool:
    s = ''.join(i for i in s if i.isalnum())
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

    # another solution
    # while l < r:
    #     if s[l] != s[r]:
    #         print('l is: ', s[l], l)
    #         print('r is: ', s[r], r)
    #         return False
    #     l += 1
    #     r -= 1
    # return True

print(is_palindrome("A man, a plan, a canal: Panama"))
