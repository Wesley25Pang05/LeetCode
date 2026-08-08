#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        dummy = curr = ListNode()
        for item in arr:
            curr.next = ListNode(item)
            curr = curr.next
        return dummy.next

# LeetCode Analysis:
# Key Idea: Merge k sorted linked lists into one sorted list using efficient merging techniques.
# Current: Array / Sorting
# Suggested: Heap (Priority Queue)
# Current complexity: O(NlogN)
# Suggested complexity: O(NlogK)
# Readability: Excellent
# Structure: Excellent
