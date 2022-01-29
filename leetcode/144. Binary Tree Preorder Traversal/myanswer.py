class Solution:
    def __init__(self):
        self.answer=[]
    def preorder(self, root: Optional[TreeNode]):
        self.answer.append(root.val)
        if(root.left!=None):
            self.preorder(root.left)
        if(root.right!=None):
            self.preorder(root.right)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root!=None):
            self.preorder(root)
        return self.answer
