class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None and list2==None):
            return None
        now=ListNode(0)
        answer=now
        while(list1!=None or list2!=None):
            if(list1==None):
                now.val=list2.val
                list2=list2.next
            elif(list2==None):
                now.val=list1.val
                list1=list1.next
            else:
                if(list1.val<list2.val):
                    now.val=list1.val
                    list1=list1.next
                else:
                    now.val=list2.val
                    list2=list2.next
            if(list1!=None or list2!=None):
                now.next=ListNode(0)
                now=now.next
        return answer
