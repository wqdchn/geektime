# @program: PyDemo
# @description: https://leetcode.com/problems/n-queens-ii/
# @author: wqdong
# @create: 2019-08-30 09:39
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return []
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位
        while bits:
            p = bits & -bits  # 取得最低位的1
            self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1) # 去掉最低位的1


s = Solution()
print(s.totalNQueens(4))
