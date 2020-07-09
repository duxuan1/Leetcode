# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL
        """
        if m == n:
            return head
        root = ListNode(0)
        root.next = head
        pre = root.next

        for i in range(m - 1):
            pre = pre.next

        rev = None
        start = pre.next
        for i in range(n - m + 1):
           next = start.next








