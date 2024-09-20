from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result array initialized to 1
        result = [1] * len(nums)

        # Left pass: Calculate the product of elements to the left of each element
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        # Right pass: Calculate the product of elements to the right of each element
        # Use a postfix variable to keep track of the running product from the right
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: General case
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1} -> Output: {solution.productExceptSelf(nums1)}")

    # Test Case 2: Array with zeroes
    nums2 = [1, 0, 3, 4]
    print(f"Input: {nums2} -> Output: {solution.productExceptSelf(nums2)}")

    # Test Case 3: All elements are 1
    nums3 = [1, 1, 1, 1]
    print(f"Input: {nums3} -> Output: {solution.productExceptSelf(nums3)}")

    # Test Case 4: Single element
    nums4 = [5]
    print(f"Input: {nums4} -> Output: {solution.productExceptSelf(nums4)}")

    # Test Case 5: Large input
    nums5 = [2, 4, 6, 8, 10]
    print(f"Input: {nums5} -> Output: {solution.productExceptSelf(nums5)}")
