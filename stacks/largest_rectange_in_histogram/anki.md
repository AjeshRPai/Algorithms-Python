###  **Anki Flash Card:**

**Question**: How do you calculate the largest rectangle in a histogram using a stack?

**Answer**:
1. Use a stack to store (index, height) of histogram bars.
2. When a shorter bar is encountered, pop the stack and calculate the area of the rectangle that can be formed using the popped height.
3. Calculate the width of the rectangle as the difference between the current index and the index of the popped height.
4. Continue this process until all bars are processed.
5. Finally, process any remaining bars in the stack.