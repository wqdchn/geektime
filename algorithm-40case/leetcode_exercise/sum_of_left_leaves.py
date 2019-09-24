# @program: PyDemo
# @description: https://leetcode.com/problems/sum-of-left-leaves/
# @author: wqdong
# @create: 2019-09-24 16:40
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left and not node.left.left and not node.left.right:
                    res.append(node.left.val)

        return sum(res)


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left.left = TreeNode(1)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(7)

# expected is 17
print(s.sumOfLeftLeaves(root))
