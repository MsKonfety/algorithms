class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res
        end = None
        while list1 and list2:
            if list1.val <= list2.val:
                res.val = list1.val
                list1 = list1.next
            else:    
                res.val = list2.val
                list2 = list2.next
            res.next = ListNode()
            end = res
            res = res.next
        while list1:
            res.val = list1.val
            list1 = list1.next
            res.next = ListNode()
            end = res
            res = res.next
        while list2:
            res.val = list2.val
            list2 = list2.next
            res.next = ListNode()
            end = res
            res = res.next
        if end:
            end.next = None    
        else:
            head = None
        return head