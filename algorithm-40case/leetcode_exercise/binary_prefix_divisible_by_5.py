class Solution:
    def prefixesDivBy5(self, nums: [int]):
        num = 0
        for k, v in enumerate(nums):
            num <<= 1
            num += v
            if(num % 5 == 0):
                nums[k] = True
            else:
                nums[k] = False
        return nums

s = Solution()
nums = [1,1,1]

print(s.prefixesDivBy5(nums))

# Runtime: 300 ms, faster than 79.03% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15 MB, less than 98.18% of Python3 online submissions for Binary Prefix Divisible By 5.