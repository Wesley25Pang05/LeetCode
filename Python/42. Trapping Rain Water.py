# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        leftMax = height[left]
        rightMax = height[right]

        trappedWater = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                trappedWater += max(0, min(leftMax, rightMax) - height[left])
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                trappedWater += max(0, min(leftMax, rightMax) - height[right])
        return trappedWater

# LeetCode Analysis:
# Key Idea: Calculate trapped water using two pointers to track max heights from both ends.
# Current: Two Pointers
# Suggested: Two Pointers / Dynamic Programming
# Current complexity: O(N)
# Suggested complexity: O(N)
# Readability: Excellent
# Structure: Excellent
