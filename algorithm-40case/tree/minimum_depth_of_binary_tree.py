# @program: PyDemo
# @description: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# @author: wqdong
# @create: 2019-08-20 11:41
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # dfs
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # bfs
    def minDepth2(self, root):
        if not root: return 0
        q = collections.deque([(root, 1)])
        while q:
            curr, depth = q.popleft()
            if not curr.left and not curr.right:
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

print(s.minDepth(root))
print(s.minDepth2(root))
