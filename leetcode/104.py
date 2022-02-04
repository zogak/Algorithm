'''
104. Maximum Depth of Binary Tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        current_node = root
        queue = collections.deque([current_node])
        cnt = 0
        
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            cnt += 1
            
        return cnt