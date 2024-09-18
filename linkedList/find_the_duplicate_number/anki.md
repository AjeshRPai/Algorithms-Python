### 3. Anki Cards to Memorize This Solution


**Front (Question)**:
**Q1**: What is the key idea behind using Floyd’s Tortoise and Hare algorithm to find a duplicate in an array?

**Back (Answer)**:
**A**: The key idea is to treat the array as a linked list where each value points to the next index, creating a cycle
due to the duplicate. Floyd’s algorithm detects the cycle, and once the cycle is found, it can identify the duplicate
number by finding the entrance to the cycle.

---

**Front (Question)**:
**Q2**: What is the purpose of the first phase in Floyd’s cycle detection algorithm in this problem?

**Back (Answer)**:
**A**: The first phase aims to detect a cycle in the array using two pointers (`slow` and `fast`). The `slow` pointer
moves one step at a time, while the `fast` pointer moves two steps. They meet inside the cycle, confirming the existence
of a duplicate.

---

**Front (Question)**:
**Q3**: How do we find the duplicate number once a cycle is detected in the array?

**Back (Answer)**:
**A**: After detecting the cycle, reset one pointer (`slow2`) to the start of the array. Move both pointers (`slow` and
`slow2`) one step at a time. The point where they meet is the duplicate number.

---

**Front (Question)**:
**Q4**: Why does resetting one pointer to the start after detecting a cycle work in finding the duplicate number?

**Back (Answer)**:
**A**: Resetting one pointer to the start works because both pointers (`slow` and `slow2`) will now be equally distant
from the cycle’s starting point (the duplicate number). When they meet, they point to the duplicate.

---

**Front (Question)**:
**Q5**: What is the time and space complexity of the Floyd's Tortoise and Hare algorithm for finding the duplicate in an
array?

**Back (Answer)**:
**A**:

- **Time complexity**: O(n), where `n` is the number of elements in the array.
- **Space complexity**: O(1), as the algorithm uses constant space.

---