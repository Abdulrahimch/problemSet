def longest_common_prefix(strs):
    strs.sort(key=len)
    max_match = strs[0]
    for i in range(1, len(strs)):
        match = longest_pre_two_strings(max_match, strs[i])
        max_match = match
    return max_match

def longest_pre_two_strings(str1, str2):
    all_matches = []
    match = ''
    max_matches = ''
    i = 0
    if str1 in str2:
        return str1
    while i < len(str1)-1:
        if match + str1[i] in str2:
            match += str1[i]
            if i == len(str1)-1:
                all_matches.append(match)
        else:
            all_matches.append(match)
            match = str1[i]
        i += 1
    try:
        max_matches = max(all_matches)
    except:
        max_matches = ""
    return max_matches

strs = ["ab", "a"]

print(longest_common_prefix(strs))