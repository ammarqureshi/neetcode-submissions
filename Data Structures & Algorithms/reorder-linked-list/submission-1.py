# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # reverse second half
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # first point to head, second pointing to reversed head
        first, second = head, prev

        while second: 
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next