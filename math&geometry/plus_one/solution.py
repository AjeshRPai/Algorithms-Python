from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start by reversing the digits to process from least significant to most significant
        digits = digits[::-1]
        carry = 1  # We need to add one, so initialize carry as 1

        i = 0
        # Loop until there is no carry left
        while carry:
            # If i is within the length of digits, process the current digit
            if i < len(digits):
                # If the current digit is 9, set it to 0 (carry over to next digit)
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    # Add 1 (the carry) to the current digit
                    digits[i] += 1
                    carry = 0  # No more carry needed
            else:
                # If we finished processing all digits and still have carry, append 1
                digits.append(1)
                carry = 0
            i += 1

        # Reverse the digits back to the original order and return
        return digits[::-1]


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: Simple case
    digits1 = [1, 2, 3]
    print(f"Input: {digits1}, Output: {solution.plusOne(digits1)}")  # Expected: [1, 2, 4]

    # Test Case 2: Case with carry over
    digits2 = [9, 9, 9]
    print(f"Input: {digits2}, Output: {solution.plusOne(digits2)}")  # Expected: [1, 0, 0, 0]

    # Test Case 3: Case with a single digit
    digits3 = [9]
    print(f"Input: {digits3}, Output: {solution.plusOne(digits3)}")  # Expected: [1, 0]

    # Test Case 4: Empty array (edge case)
    digits4 = []
    print(f"Input: {digits4}, Output: {solution.plusOne(digits4)}")  # Expected: [1]


