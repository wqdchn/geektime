# @program: PyDemo
# @description: https://leetcode.com/problems/pascals-triangle/
# @author: wqdong
# @create: 2020-01-28 10:16

class Solution:

    # Runtime: 28 ms, faster than 66.99% of Python3 online submissions for Pascal's Triangle.
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle


sl = Solution()
numRows = 5
for tri in sl.generate(numRows):
    print(tri)
