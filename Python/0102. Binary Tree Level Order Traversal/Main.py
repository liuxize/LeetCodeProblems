# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            l = len(stack)
            tmp = []
            for i in range (l):
                s = stack.pop(0)
                if s.left:
                    stack.append(s.left)
                if s.right:
                    stack.append(s.right)
                tmp.append(s.val)
            res.append(tmp)
        return res 
