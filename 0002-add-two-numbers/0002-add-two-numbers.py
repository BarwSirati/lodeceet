class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumOfNum1 = ""
        sumOfNum2 = ""
        while l1:
            sumOfNum1 += str(l1.val)
            l1 = l1.next
        while l2:
            sumOfNum2 += str(l2.val)
            l2 = l2.next
        result = str(int(sumOfNum1[::-1]) + int(sumOfNum2[::-1]))[::-1]
        d = l = ListNode(0)
        for i in result:
            l.next = ListNode(int(i))
            l = l.next
        return d.next

           