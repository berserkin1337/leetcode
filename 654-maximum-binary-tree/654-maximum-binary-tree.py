# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    
        def ans(i,j):
            if j<i:
                return None
            if i==j:
                node = TreeNode(nums[i])
                return node
            val = max(nums[i:j+1])
            idx = nums[i:j+1].index(val) + i
            # print(i,j,val)
            # node = TreeNode(val)
            left= None
            if (idx-1) >= i:
                left = ans(i,idx-1)
            right = None
            if (idx+1<=j):
                right = ans(idx+1,j)
            node = TreeNode(val,left,right)
            return node
        return ans(0,len(nums) - 1)