# @program: PyDemo
# @description: https://leetcode.com/problems/same-tree/
# @author: wqdong
# @create: 2020-01-27 14:04


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Runtime: 28 ms, faster than 69.63% of Python3 online submissions for Same Tree.
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


sl = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

if sl.isSameTree(p, q):
    print("True")
else:
    print("False")
