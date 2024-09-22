### **Key Points to Memorize:**

- **Stack to track bars**: The stack keeps track of (index, height) for bars, allowing us to efficiently compute areas as we encounter shorter bars.
- **Pop when height decreases**: If the current bar is shorter than the bar on top of the stack, pop the stack and compute the area.
- **Calculate area based on width**: For each popped bar, the width of the rectangle is determined by the difference between the current index and the index of the popped bar.
- **Final pass through stack**: After processing all bars, calculate areas for any remaining bars in the stack.

