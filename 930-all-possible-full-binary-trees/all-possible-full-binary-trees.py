class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return [TreeNode(0, left, right) for k in range(1, n-1, 2) for left in self.allPossibleFBT(k) for right in self.allPossibleFBT(n-1-k)] if n != 1 else [TreeNode()]