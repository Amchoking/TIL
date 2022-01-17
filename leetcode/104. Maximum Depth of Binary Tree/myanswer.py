class Solution:
    def depthcheck(self,now: TreeNode, count: int) -> int:
        if(now==None):
            return count
        return max(self.depthcheck(now.left,count+1),self.depthcheck(now.right,count+1))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepths=self.depthcheck(root,0)
        return maxdepths
