from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array for simplicity
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2

        left, right = 0, len(nums1) - 1

        while True:
            # Calculate partition points
            partition1 = (left + right) // 2
            partition2 = half_length - partition1 - 2

            # Get values at partition points (use infinity for out-of-bounds)
            left1 = nums1[partition1] if partition1 >= 0 else float("-infinity")
            right1 = nums1[partition1 + 1] if (partition1 + 1) < len(nums1) else float("infinity")
            left2 = nums2[partition2] if partition2 >= 0 else float("-infinity")
            right2 = nums2[partition2 + 1] if (partition2 + 1) < len(nums2) else float("infinity")

            # Check if we've found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is odd, return the smaller of the two middle values
                if total_length % 2:
                    return min(right1, right2)
                # If total length is even, return average of two middle values
                return (max(left1, left2) + min(right1, right2)) / 2

            # Adjust partition if not correct
            if left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1


if __name__ == '__main__':
    solution = Solution()

    # Test case 1: Both arrays non-empty, even total length
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0

    # Test case 2: Both arrays non-empty, odd total length
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5

    # Test case 3: One empty array
    assert solution.findMedianSortedArrays([], [1]) == 1.0

    # Test case 4: Arrays of different lengths
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.0

    # Test case 5: Negative numbers
    assert solution.findMedianSortedArrays([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]) == 3.0

    # Test case 6: Large numbers
    assert solution.findMedianSortedArrays([100000], [100001]) == 100000.5

    # Test case 7: Duplicate numbers
    assert solution.findMedianSortedArrays([1, 2, 3, 3], [1, 2, 3, 4]) == 2.5

    print("All tests passed!")

