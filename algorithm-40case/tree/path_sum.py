# @program: PyDemo
# @description: https://leetcode.com/problems/path-sum/
# @author: wqdong
# @create: 2020-01-17 09:28

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Runtime: 28 ms, faster than 99.67% of Python3 online submissions for Path Sum.
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sum = 22

if s.hasPathSum(root, sum):
    print("Has path sum.")
else:
    print("Not has path sum.")