class Solution:
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            if i not in dic.keys(): dic[i] = 1
            else: dic[i] += 1
        for i in dic:
            if dic[i] < 2:
                return i