# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1

        while l2:
            curr.val += l2.val

            if curr.val > 9:
                curr.val -= 10
                if curr.next:
                    curr.next.val += 1
                else:
                    curr.next = ListNode(1)

            if curr.next:
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l2.next
                curr = curr.next
                break

        while curr:
            if curr.val > 9:
                curr.val -= 10
                if curr.next:
                    curr.next.val += 1
                else:
                    curr.next = ListNode(1)
            curr = curr.next

        return l1

# LeetCode Analysis:
# Key Idea: Simulate addition digit by digit on linked lists, handling carry propagation efficiently.
# Current: Linked List / Simulation
# Suggested: Linked List / Simulation
# Current complexity: O(max(N,M))
# Suggested complexity: O(max(N,M))
# Readability: Excellent
# Structure: Excellent
