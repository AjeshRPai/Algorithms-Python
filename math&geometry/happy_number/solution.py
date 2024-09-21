class Solution:
    def isHappy(self, n: int) -> bool:
        # Initialize slow and fast pointers
        slow, fast = n, self.sumSquareDigits(n)

        # Detect cycle using Floyd’s Cycle Detection Algorithm
        while slow != fast:
            # Move the fast pointer two steps ahead
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            # Move the slow pointer one step ahead
            slow = self.sumSquareDigits(slow)

        # If fast pointer reaches 1, it's a happy number
        return fast == 1

    def sumSquareDigits(self, n: int) -> int:
        # Sum the squares of digits of n
        output = 0
        while n > 0:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: Happy number
    n1 = 19
    print(f"Is {n1} a happy number? {solution.isHappy(n1)}")  # Expected: True

    # Test Case 2: Not a happy number
    n2 = 20
    print(f"Is {n2} a happy number? {solution.isHappy(n2)}")  # Expected: False

    # Test Case 3: Edge case with single digit
    n3 = 1
    print(f"Is {n3} a happy number? {solution.isHappy(n3)}")  # Expected: True

    # Test Case 4: Larger number
    n4 = 7
    print(f"Is {n4} a happy number? {solution.isHappy(n4)}")  # Expected: True


