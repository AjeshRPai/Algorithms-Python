###  Key Points to Memorize this Solution

1. **Monotonic Stack:**
    - This problem uses a stack to track indices of temperatures. The stack maintains a decreasing order of temperatures
      as you iterate through the list.

2. **When to Update Results:**
    - For each temperature in the list, while the current temperature is greater than the temperature at the top of the
      stack, you pop the stack. For each popped item, the difference between the current index and the popped index is
      the number of days until a warmer temperature.

3. **Stack Entries:**
    - Each entry in the stack is a tuple of `(temperature, index)`. You store the index to compute the difference in
      days later.

4. **No Warmer Day:**
    - If there's no future warmer day for a temperature, the corresponding result stays `0` (as initialized).

5. **Time Complexity:**
    - The time complexity is `O(n)` because each temperature is pushed and popped from the stack at most once.
