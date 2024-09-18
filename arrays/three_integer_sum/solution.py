from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to enable two-pointer technique

        for i, a in enumerate(nums):
            # If the current number is greater than 0, break the loop
            if a > 0:
                break  # No valid triplet can sum to 0 if 'a' is positive

            # Skip the same element to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Use two pointers: left (l) and right (r)
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                # If the sum is greater than 0, move the right pointer left
                if threeSum > 0:
                    r -= 1
                # If the sum is less than 0, move the left pointer right
                elif threeSum < 0:
                    l += 1
                # If the sum is exactly 0, we found a valid triplet
                else:
                    res.append([a, nums[l], nums[r]])  # Add the triplet to the result
                    l += 1
                    r -= 1

                    # Skip duplicates for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [0, -1, 1, 2, -1, -4],   # Standard case with multiple triplets
        [1, 2, -2, -1],           # Case with no valid triplets
        [0, 0, 0, 0],             # Case with all zeros
        [-1, 0, 1, 2, -1, -4],   # Case with repeated elements
        [3, -2, 1, 0, -1, 2],     # Case with both positive and negative numbers
        [-1, 0, 1, 0]             # Case with fewer elements
    ]

    for nums in test_cases:
        result = solution.threeSum(nums)
        print(f"Input: {nums} => Triplets: {result}")