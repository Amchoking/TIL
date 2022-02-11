class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root1==None):
            return root2
        if(root2==None):
            return root1
        answer=TreeNode()
        def merge(root1: Optional[TreeNode], root2: Optional[TreeNode], root3: Optional[TreeNode]):
            root3.val=root1.val+root2.val
            if(root1.left==None or root2.left==None):
                if(root1.left==None):
                    root3.left=root2.left
                else:
                    root3.left=root1.left
            else:
                root3.left = TreeNode()
                merge(root1.left,root2.left,root3.left)
            if(root1.right==None or root2.right==None):
                if(root1.right==None):
                    root3.right=root2.right
                else:
                    root3.right=root1.right
            else:
                root3.right = TreeNode()
                merge(root1.right,root2.right,root3.right)
        merge(root1,root2,answer)
        return answer
