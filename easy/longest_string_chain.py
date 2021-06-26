def longestStrChain(words):
    words_dic = {}
    longest = 0
    words.sort(key=len)

    for i in words:
        words_dic[i] = 1

    for word in words:
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]

            if temp in words_dic:
                words_dic[word] = words_dic[temp] +1

            if words_dic[word] > longest: longest = words_dic[word]
    return longest


print(longestStrChain(["a","b","ba","bca","bda","bdca"]))