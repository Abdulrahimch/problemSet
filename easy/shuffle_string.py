# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

def shuffle_string(s, indices):
    dic = {n: s[idx] for idx, n in enumerate(indices)}
    return ''.join(dic[i] for i in range(len(s)))

print(shuffle_string("codeleet", [4,5,6,7,0,2,1,3]))