###  **Anki Flash Card:**

**Question**: How do you determine if a number is a happy number using Floyd’s Cycle Detection?

**Answer**:
1. A number is happy if the sum of squares of its digits eventually leads to 1.
2. Use two pointers (slow and fast):
   - Slow pointer: moves one step (one sum of squares) at a time.
   - Fast pointer: moves two steps (two sums of squares) at a time.
3. If the slow and fast pointers meet at 1, it's a happy number.
4. If they meet at any number other than 1, the number is not happy (cycle detected).
5. Use a helper function to calculate the sum of squares of digits.