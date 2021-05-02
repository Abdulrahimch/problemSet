def word_in_text(s: str, t: str) -> bool:
    # for i in s:
    #     if i == t[0]:
    #         index = s.index(i)
    #         match = ''
    #         # Avoid index out of range error!
    #         if (index + len(t)) > len(s):
    #             break
    #
    #         for j in range(index, (index + len(t))):
    #             match += s[j]
    #         if match == t:
    #             return True
    #
    # return False
    i = 0
    while i < len(s):
        if s[i] == t[0]:
            temp = s[i:i+len(t)]
            if temp == t:
                return True
            i += len(t)-1
        i+=1
    return False

str1, str2 = 'sddfabooodfmgabo', 'aboood'
print(word_in_text(str1, str2))
