class Solution:
    def __init__(self):
        self.answer=[]
    def postorder(self, root: Optional[TreeNode]):
        if(root.left!=None):
            self.postorder(root.left)
        if(root.right!=None):
            self.postorder(root.right)
        self.answer.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root!=None):
            self.postorder(root)
        return self.answer
