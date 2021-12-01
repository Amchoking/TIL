# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        head1 = l1
        head2 = l2
        over10 = 0
        
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
                
            result.append((value1+value2+over10)%10)
            over10 = (value1+value2+over10)//10
        
        if (over10):
            result.append(1)
        
        l3 = ListNode()
        head = l3
        for i in range(len(result)):
            head.val = result[i]
            if (i == len(result)-1):
                head.next = None
                break
            head.next = ListNode()
            head = head.next
        
        return l3
