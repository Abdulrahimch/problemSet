# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.

def valid_palindrome(s: str) -> bool:
    s = ''.join(i for i in s if i.isalnum())
    s = s.lower()
    l = 0
    r = len(s) - 1
    counter = 0
    if len(s) <= 2:
        return True

    if len(s) <=3:
        if s[l] != s[r]:
            return False

    while l < r:
        if s[l] != s[r]:
            counter += 1
            if counter > 1:
                return False
            if s[l] == s[r - 1]:
                l -= 1
            elif s[l + 1] == s[r]:
                r += 1
            else:
                return False
        l += 1
        r -= 1
    return True

print(valid_palindrome('tebbem'))
