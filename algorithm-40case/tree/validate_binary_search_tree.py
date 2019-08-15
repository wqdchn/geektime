# @program: PyDemo
# @description: https://leetcode.com/problems/validate-binary-search-tree/
# @author: wqdong
# @create: 2019-08-15 11:43

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root: TreeNode):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    # # 中序遍历

    def isValidBST2(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return  True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

    #递归
    def isValidBST3(self, root):

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

s = Solution()

# Example 1:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

if s.isValidBST3(root):
    print("is BST!")
else:
    print("not BST!")

# Example 2:

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

if s.isValidBST2(root):
    print("is BST!")
else:
    print("not BST!")