# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

# LeetCode Analysis:
# Key Idea: Find the smallest missing positive integer using in-place indexing.
# Current: Hash Table
# Suggested: Array
# Current complexity: O(N)
# Suggested complexity: O(N)
# Readability: Excellent
# Structure: Excellent
