###  **Anki Flash Card:**

**Question**: How do you add 1 to a number represented as an array of digits?

**Answer**:
1. Reverse the digits to process from least significant to most significant.
2. Initialize carry as 1 since you're adding one.
3. For each digit:
   - If the digit is 9, set it to 0 (carry over to the next digit).
   - Otherwise, add the carry (1) to the digit and stop carrying.
4. If all digits are processed and there's still carry, append 1 to the list.
5. Reverse the digits again to restore the original order.