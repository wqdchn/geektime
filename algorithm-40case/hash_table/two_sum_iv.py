# @program: PyDemo
# @description: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# @author: wqdong
# @create: 2020-01-26 16:41

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Runtime: 132 ms, faster than 8.57% of Python3 online submissions for Two Sum IV - Input is a BST.
    def findTarget(self, root, k):
        q, seen = [root], set()
        while q:
            curr = q.pop()
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False

    # Runtime: 104 ms, faster than 14.07% of Python3 online submissions for Two Sum IV - Input is a BST.
    def findTarget2(self, root, k):
        seen = set()
        return self.find(root, k, seen)

    def find(self, root, k, seen):
        if not root: return False
        if k - root.val in seen: return True
        seen.add(root.val)
        return self.find(root.left, k, seen) or self.find(root.right, k, seen)


sl = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

target = 9

if sl.findTarget(root, target):
    print("True")
else:
    print("False")

if sl.findTarget2(root, target):
    print("True")
else:
    print("False")
