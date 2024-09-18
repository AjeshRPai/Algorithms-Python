### 3. Anki Cards to Memorize This Solution

---

**Front (Question)**:
**Q1**: What is the key approach used to solve the 3Sum problem efficiently?

**Back (Answer)**:
**A**: The key approach is to sort the array and use a two-pointer technique. For each number in the sorted array, we
try to find two other numbers whose sum equals the negative of the current number. This allows us to efficiently find
triplets that sum to zero.

---

**Front (Question)**:
**Q2**: Why do we sort the array in the 3Sum solution?

**Back (Answer)**:
**A**: Sorting simplifies checking for duplicate triplets and allows the use of a two-pointer approach, where we can
efficiently find pairs of numbers that sum to a specific value by moving pointers in opposite directions.

---

**Front (Question)**:
**Q3**: How do we handle duplicates in the 3Sum problem?

**Back (Answer)**:
**A**: To avoid duplicate triplets:

- In the outer loop, we skip consecutive duplicate numbers.
- After finding a valid triplet, we move the left pointer while skipping over duplicate values to ensure we don’t add
  the same triplet again.

---

**Front (Question)**:
**Q4**: What happens if the current number `a` in the 3Sum solution is greater than 0?

**Back (Answer)**:
**A**: If the current number `a` is greater than 0, we can stop the loop early. Since the array is sorted and all
numbers after `a` will also be positive, there’s no way to form a triplet that sums to zero.

---

**Front (Question)**:
**Q5**: What is the time complexity of the 3Sum solution?

**Back (Answer)**:
**A**: The time complexity of the 3Sum solution is **O(n^2)**, where `n` is the number of elements in the array. This is
because we iterate over each element in the array and use the two-pointer technique, which takes linear time for each
element.

---

These Anki cards will help you solidify your understanding of the 3Sum problem-solving approach and the key steps in the
algorithm.