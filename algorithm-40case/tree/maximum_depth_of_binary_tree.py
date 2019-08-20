# @program: PyDemo
# @description: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# @author: wqdong
# @create: 2019-08-20 10:34
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # recursively
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # dfs
    def maxDepth2(self, root):
        if not root: return 0
        q = collections.deque([(root, 1)])
        while q:
            curr, depth = q.popleft()
            if not curr.left and not curr.right and not q:
                return depth
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.maxDepth(root))
print(s.maxDepth2(root))