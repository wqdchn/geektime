# @program: PyDemo
# @description: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# @author: wqdong
# @create: 2019-08-15 20:17
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in {None, p, q}:
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if (left and right) else (left or right)

s = Solution()

# Example 1:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

p = root.left
q = root.right

print(s.lowestCommonAncestor(root, p, q).val)