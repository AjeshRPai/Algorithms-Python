### Key Points to Memorize this Solution

1. **Use of Hash Sets**:
    - For each number in the board, track its occurrence in three sets: one for rows, one for columns, and one for 3x3
      subgrids.

2. **Efficient Conflict Detection**:
    - The key idea is to check if any number appears more than once in its row, column, or 3x3 subgrid.

3. **Skip Empty Cells**:
    - Cells marked with `.` are ignored since they don't contain any numbers.

4. **3x3 Subgrid Tracking**:
    - Use `(r // 3, c // 3)` to uniquely identify the 3x3 subgrid for each number, so numbers in the same subgrid are
      checked together.

5. **Return Early**:
    - The function returns `False` as soon as it detects an invalid entry, improving efficiency by not needing to check
      the entire board.

