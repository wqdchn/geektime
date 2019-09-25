# @program: PyDemo
# @description: https://leetcode.com/problems/trapping-rain-water/
# @author: wqdong
# @create: 2019-09-25 13:26

#               *
#       *       * *   *
#   *   * *   * * * * * *
# 0 1 2 3 4 5 6 7 8 9 0 1
# l                     r

class Solution:
    def trap(self, height):
        if len(height) == 0: return 0
        left, right, res, leftMax, rightMax = 0, len(height) - 1, 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
                right -= 1
        return res

    def trap2_1(self, height):
        res, curr, stack = 0, 0, []
        while curr < len(height):
            while stack and height[curr] > height[stack[-1]]:
                top = height[stack.pop()]
                if not stack: break
                distance = curr - stack[-1] - 1
                h = min(height[curr], height[stack[-1]]) - top
                res += distance * h
            stack.append(curr)
            curr += 1
        return res

    def trap2_2(self, height):
        res, stack = 0, []
        for i, v in enumerate(height):
            while stack and v > height[stack[-1]]:
                top = height[stack.pop()]
                if not stack: break
                width = i - stack[-1] - 1
                high = min(v, height[stack[-1]]) - top
                res += width * high
            stack.append(i)
        return res


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height))
print(s.trap2_1(height))
print(s.trap2_2(height))
