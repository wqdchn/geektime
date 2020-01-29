# @program: PyDemo
# @description: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# @author: wqdong
# @create: 2020-01-29 10:00

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Runtime: 68 ms, faster than 76.25% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST(self, nums):  # O(nlogn)
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])  # 切片操作时间复杂度O(n)
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    # Runtime: 72 ms, faster than 51.68% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST1(self, nums):
        return self.dfs_helper1(nums, 0, len(nums) - 1)

    def dfs_helper1(self, nums, left, right):
        if left > right: return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs_helper1(nums, left, mid - 1)
        root.right = self.dfs_helper1(nums, mid + 1, right)
        return root

    # Runtime: 64 ms, faster than 90.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST2(self, nums):
        return self.dfs_helper2(nums, 0, len(nums))

    def dfs_helper2(self, nums, left, right):
        if left >= right: return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs_helper2(nums, left, mid)
        root.right = self.dfs_helper2(nums, mid + 1, right)
        return root

    def preOrder(self, root):
        if root:
            print(root.val, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)


sl = Solution()
nums = [-10, -3, 0, 5, 9]
root = sl.sortedArrayToBST(nums)
sl.preOrder(root)

print()
root1 = sl.sortedArrayToBST1(nums)
sl.preOrder(root1)

print()
root2 = sl.sortedArrayToBST2(nums)
sl.preOrder(root2)

# 0 -3 -10 9 5
# 0 -10 -3 5 9
# 0 -3 -10 9 5