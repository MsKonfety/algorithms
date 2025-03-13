
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        counter = {}
        cur = head
        while cur:
            if cur.val in counter:
                counter[cur.val] += 1
            else:
                counter[cur.val] = 1
            cur = cur.next
        
        ans = ListNode(0)
        cur = ans
        while head:
            if counter[head.val] == 1: 
                cur.next = head
                cur = cur.next
            head = head.next
        return ans.next