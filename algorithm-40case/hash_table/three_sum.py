# @program: PyDemo
# @description: https://leetcode.com/problems/3sum/
# @author: wqdong
# @create: 2019-08-14 11:29

class Solution:
    def threeSum(self, nums):
        if len(nums) < 0: return []

        nums.sort() #有序
        res = set()

        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue #在有序的情况下存在前后相等则跳过进下一轮
            d = {}
            for x in nums[i+1:]: #遍历后面的数
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))

s = Solution()
nums = [-1, 0, 1, 2, -1, -4, 4]

print(s.threeSum(nums))