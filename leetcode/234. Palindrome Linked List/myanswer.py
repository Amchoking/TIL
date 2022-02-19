class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        checkstr=""
        now=head
        while(now):
            checkstr=checkstr+str(now.val)
            now=now.next
        if(checkstr==checkstr[::-1]):
            return True
        return False
