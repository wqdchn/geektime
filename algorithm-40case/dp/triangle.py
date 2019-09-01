# @program: PyDemo
# @description: https://leetcode.com/problems/triangle/
# @author: wqdong
# @create: 2019-09-01 09:41


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        res = triangle[-1] # 三角形最后一行赋给res, 自底向上进行计算
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


s = Solution()
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(s.minimumTotal(triangle))
