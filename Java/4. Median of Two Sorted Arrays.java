/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
*/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalLength = nums1.length + nums2.length;
        int[] nums3 = new int[(totalLength + 2) / 2];
        int one = 0;
        int two = 0;
        for (int i = 0; i < nums3.length; i++) {
            if (nums1.length - 1 < one) {
                nums3[i] = nums2[two];
                two++;
            }
            else if (nums2.length - 1 < two) {
                nums3[i] = nums1[one];
                one++;
            }
            else if (nums1[one] < nums2[two]) {
                nums3[i] = nums1[one];
                one++;
            }
            else {
                nums3[i] = nums2[two];
                two++;
            }
        }
        if (totalLength % 2 == 1) return nums3[totalLength / 2];
        return (nums3[totalLength / 2 - 1] + nums3[totalLength / 2]) / 2.0;
    }
}

/*
LeetCode Analysis:
Key Idea: Finding median of two sorted arrays using merging or binary search partitioning.
Current: Array / Two Pointers
Suggested: Binary Search / Array
Current complexity: O(M+N)
Suggested complexity: O(log(M+N))
Readability: Excellent
Structure: Excellent
*/
