def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ("")
    if len(strs) == 1:
        return (strs[0])

    prefix = strs[0]
    previous_length = len(prefix)

    for str in strs[1:]:
        while prefix != str[0:previous_length]:
            prefix = prefix[0:(previous_length-1)]
            previous_length -= 1

            if previous_length == 0:
                return ("")

    return(prefix)

print(longestCommonPrefix(['flower', 'flow', 'raflowsd']))

