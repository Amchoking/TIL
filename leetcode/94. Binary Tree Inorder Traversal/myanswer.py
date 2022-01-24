class Solution:
    def __init__(self):
        self.answer=[]
    def inorder(self, root: Optional[TreeNode]):
        if(root.left!=None):
            self.inorder(root.left)
        self.answer.append(root.val)
        if(root.right!=None):
            self.inorder(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root!=None):
            self.inorder(root)
        return self.answer
