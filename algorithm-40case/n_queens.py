# @program: PyDemo
# @description: https://leetcode.com/problems/n-queens/
# @author: wqdong
# @create: 2019-08-22 11:01


class Solution:
    def solveNQueens(self, n: int):
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])
        result = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


s = Solution()
print(s.solveNQueens(4))