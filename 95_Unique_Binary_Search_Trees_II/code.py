# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 2023/08/04 23:09PM -> 23:36PM
        dp = {}
        def dfs(l, r) -> List[TreeNode]:
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            if (l, r) not in dp:
                res = []
                for root in range(l, r + 1):
                    for l_tree in dfs(l, root - 1):
                        for r_tree in dfs(root + 1, r):
                            res.append(TreeNode(root, l_tree, r_tree))
                dp[(l, r)] = res
            return dp[(l, r)]
        return dfs(1, n)