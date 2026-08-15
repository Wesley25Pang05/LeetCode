# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, j in enumerate(nums):
            if j not in sums:
                sums[target - j] = i
            else:
                return [sums[j], i]

# LeetCode Analysis:
# Key Idea: Use a hash table to store complements for O(1) lookups.
# Current: Hash Table
# Suggested: Hash Table
# Current complexity: O(N)
# Suggested complexity: O(N)
# Readability: Excellent
# Structure: Excellent
