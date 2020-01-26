# @program: PyDemo
# @description: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# @author: wqdong
# @create: 2020-01-26 10:29

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # bfs
    # Runtime: 24 ms, faster than 98.01% of Python3 online submissions for Binary Tree Level Order Traversal II.
    def levelOrderBottom(self, root: TreeNode):
        if not root: return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.insert(0, current_level)
        return res

    # dfs
    # Runtime: 36 ms, faster than 39.83% of Python3 online submissions for Binary Tree Level Order Traversal II.
    def levelOrderBottom2(self, root: TreeNode):
        if not root: return []
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if not node: return

        if len(self.res) <= level:
            self.res.insert(0, [])

        self.res[-(level + 1)].append(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)


sl = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sl.levelOrderBottom(root))
print(sl.levelOrderBottom2(root))
