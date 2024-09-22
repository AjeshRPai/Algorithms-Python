### **Key Points to Memorize:**

- **Two-pointer technique**: Start with two pointers at both ends of the array (`l` and `r`), and move them towards each other.
- **Track maximum boundaries**: Use `leftMax` and `rightMax` to keep track of the highest barriers on each side.
- **Water calculation**: Water trapped at any position is the difference between the maximum boundary and the height at that position.
- **Stop condition**: The loop continues until the two pointers meet.
  
