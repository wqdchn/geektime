# @program: PyDemo
# @description: https://leetcode.com/problems/container-with-most-water/
# @author: wqdong
# @create: 2019-11-05 08:48

class Solution:
    def maxArea_1(self, height):  # Time Limit Exceeded
        result = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                result = max(result, min(height[i], height[j]) * (j - i))
        return result

    def maxArea_2(self, height): # Runtime: 152 ms, faster than 36.03%
        result, left, right = 0, 0, len(height) - 1
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result

    def maxArea_3(self, height): # Runtime: 144 ms, faster than 72.17%
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            if area > result:
                result = area

        return result


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea_1(height))
print(s.maxArea_2(height))
print(s.maxArea_3(height))
