# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        prev = None
        num = k

        while curr and k > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1

        if k == 0:
            head.next = self.reverseKGroup(curr, num)
        else:
            return self.reverseKGroup(prev, num - k)

        return prev

# LeetCode Analysis:
# Key Idea: Reverse linked list nodes in groups of k using pointer manipulation.
# Current: Linked List / Recursion
# Suggested: Linked List / Two Pointers
# Current complexity: O(N)
# Suggested complexity: O(N)
# Readability: Excellent
# Structure: Excellent
