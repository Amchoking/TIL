# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head1 = l1
        head2 = l2
        over10 = 0
        l3 = result
        
        while not ((head1 is None) and (head2 is None)):
            if (head1 is None):
                value1 = 0
            else:
                value1 = head1.val
                head1 = head1.next
                
            if (head2 is None):
                value2 = 0
            else:
                value2 = head2.val
                head2 = head2.next
                
            result.val = ((value1+value2+over10)%10)
            over10 = (value1+value2+over10)//10
            if (over10 or head1 or head2):
                result.next = ListNode()
                result = result.next
        
        if (over10):
            result.val = 1
            result.next = None
        else:
            result.next = None
        
        return l3
