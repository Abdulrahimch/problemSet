def is_anagram(s: str, t: str) -> bool:
    for i in t:
        if i not in s:
            return False

    return True

s, t = "anagram", "nagaram"
str1, str2 = 'apple', 'apitte'
print(is_anagram(s, t))
print(is_anagram(str1, str2))
