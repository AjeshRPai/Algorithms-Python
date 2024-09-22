### **Anki Flash Card:**

**Question**: How do you calculate trapped rainwater given an array?

**Answer**:
1. Start with two pointers at the beginning and end of the array (`l`, `r`).
2. Track the max height on the left (`leftMax`) and right (`rightMax`).
3. Move the pointer corresponding to the smaller boundary and calculate the trapped water at that position.
4. Add the difference between the current height and the maximum boundary height to the result.
5. Continue until the pointers meet.