# @program: PyDemo
# @description: https://leetcode.com/problems/construct-string-from-binary-tree/
# @author: wqdong
# @create: 2019-11-20 15:24

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None: return ""
        if t.left == None and t.right == None: return t.val + ""
        if t.right == None: return t.val + "(" + self.tree2str(t.left) + ")"
        return t.val + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"


s = Solution()

t = TreeNode("1")
t.left = TreeNode("2")
t.right = TreeNode("3")
t.left.left = TreeNode("4")

print(s.tree2str(t))
