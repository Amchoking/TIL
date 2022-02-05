class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        check=0
        now=head
        while(now!=None):
            check=check+1
            now=now.next
        if(check==n):
            return head.next
        reset=head
        for i in range(check-n-1):
            reset=reset.next
        reset.next = reset.next.next
        return head
