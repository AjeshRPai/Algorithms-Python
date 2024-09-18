
###  Key Points and Visualization

#### **Key Points**:

1. **Cycle Detection**: Treat the array as a linked list, where `nums[i]` points to the next index, creating a cycle
   because one number is duplicated.
2. **Two Pointer Approach**:
    - **Phase 1**: Use two pointers (`slow` and `fast`). `Slow` moves one step at a time, `fast` moves two steps. They
      meet when they enter the cycle.
    - **Phase 2**: Once a cycle is detected, reset one pointer (`slow2`) to the start and move both pointers one step at
      a time to find the duplicate.
3. **Entrance of the Cycle**: The first node where the two pointers meet in the second phase is the duplicate number.

#### **Visualization**:

Imagine an array `[1, 3, 4, 2, 2]`. The array can be visualized as a graph:

```
Index:   0 -> 1 -> 2 -> 3 -> 4
Values: [1]  [3]  [4]  [2]  [2]
           ^             |
           |-------------|
```

- **Cycle Detection**: The `slow` and `fast` pointers will eventually meet at index `2` (since the value `2` is
  duplicated).
- **Finding Duplicate**: Reset one pointer (`slow2`) to the start and move both one step at a time. They will meet at
  the value `2`, which is the duplicate.

---
