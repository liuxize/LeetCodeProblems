# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return  1 + self.minDepth(root.right)
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        #if not root.left and not root.right: 为什么加上这句话不行
        return 1 + min((self.minDepth(root.left), self.minDepth(root.right)))
        