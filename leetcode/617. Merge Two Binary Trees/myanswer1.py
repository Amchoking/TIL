class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root1==None and root2==None):
            return None
        answer=TreeNode()
        def merge(root1: Optional[TreeNode], root2: Optional[TreeNode], root3: Optional[TreeNode]):
            if(root1!=None and root2!=None):
                root3.val=root1.val+root2.val
                if(root1.left!=None or root2.left!=None):
                    root3.left=TreeNode()
                    merge(root1.left,root2.left,root3.left)
                if(root1.right!=None or root2.right!=None):
                    root3.right=TreeNode()
                    merge(root1.right,root2.right,root3.right)
            elif(root2!=None):
                root3.val=root2.val
                if(root2.left!=None):
                    root3.left=TreeNode()
                    merge(None,root2.left,root3.left)
                if(root2.right!=None):
                    root3.right=TreeNode()
                    merge(None,root2.right,root3.right)
            elif(root1!=None):
                root3.val=root1.val
                if(root1.left!=None):
                    root3.left=TreeNode()
                    merge(root1.left,None,root3.left)
                if(root1.right!=None):
                    root3.right=TreeNode()
                    merge(root1.right,None,root3.right)
        merge(root1,root2,answer)
        return answer
