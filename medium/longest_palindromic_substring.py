def longestPalindrome(s):

    if len(s) < 2:
        return s[0]

    result = []
    for i in range(len(s)):
        j = len(s)
        while j > i:
            bck = s[i:j]
            if bck == bck[::-1]:
                result.append(bck)
                break
            j -= 1
    return max(result, key=len)