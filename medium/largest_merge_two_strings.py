def largestMerge(word1, word2):
    word1_len = len(word1)
    merge = ''
    word1_backup = word1
    if len(word2) < len(word1):
        word1, word2 = word2, word1

    while word1 or word2:
        while word1 != word2[:word1_len]:
            word1 = word1[:word1_len-1]
            word1_len -= 1

            if word1_len == 0:
                word1_backup = word1
                i = 0
                while word1 and word2:
                    if word1[i] > word2[i]:
                        merge += word1[i]
                        word1 = word1[i+1:]
                    else:
                        merge += word2[i]
                        word2 = word2[i+1:]
                    i += 1

                if word1: merge += word1
                else: merge += word2
                word1, word2 = '', ''

        print('word1 is ', word1)
        print('word2 is: ', word2)
        print('word2[:word1_len] is: ', word2[:word1_len])
        print(word1_backup)
        if word1_backup[:word1_len+1] > word2[:word1_len+1]:
            merge += word1_backup[:word1_len+1]
            word1 = word1_backup
            word1_backup = word1
            word1_len = len(word1)
        else:
            print('len is: ', word1_len)
            merge += word2[:word1_len+1]
            word2 = word2[word1_len+1:]
            word1_len = len(word2)
            word1 = word1_backup
            print('merge from else ', merge)


    print(merge)

largestMerge('abcabc', 'abdcaba')