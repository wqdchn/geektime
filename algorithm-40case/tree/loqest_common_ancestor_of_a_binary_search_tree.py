# @program: PyDemo
# @description: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# @author: wqdong
# @create: 2019-08-16 14:32
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if root in {None, p, q}:
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if (left and right) else (left or right)

    def lowestCommonAncestor2(self, root:TreeNode, p:TreeNode, q:TreeNode):
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        if p.val > root.val < q.val:
            return  self.lowestCommonAncestor2(root.right, p, q)
        return  root

    def lowestCommonAncestor3(self, root: TreeNode, p: TreeNode, q: TreeNode):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            if p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
s = Solution()

# Example 1:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

p = root.left
q = root.right

print(s.lowestCommonAncestor3(root, p, q).val)