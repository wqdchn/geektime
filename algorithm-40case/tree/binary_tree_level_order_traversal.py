# @program: PyDemo
# @description: https://leetcode.com/problems/binary-tree-level-order-traversal/
# @author: wqdong
# @create: 2019-08-19 14:14

# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # bfs
    def levelOrder(self, root: TreeNode):
        if not root: return []

        res = []
        queue = collections.deque()
        queue.append(root)

        # visited = set(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(current_level)
        return res

    # dfs
    def levelOrder2(self, root: TreeNode):
        if not root: return []
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if not node: return

        if len(self.res) < level + 1:
            self.res.append([])

        self.res[level].append(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.levelOrder(root))
print(s.levelOrder2(root))