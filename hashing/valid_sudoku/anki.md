### Anki Card Based on Key Points

#### Front

What are the key steps to validate if a Sudoku board is valid?

#### Back

1. **Use Hash Sets**:
    - Track seen numbers in three sets: one for rows, one for columns, and one for 3x3 subgrids.

2. **Check for Conflicts**:
    - Check if a number has already been seen in its row, column, or 3x3 subgrid. If so, return `False`.

3. **Skip Empty Cells**:
    - Ignore cells that contain `.` as they don't affect the Sudoku's validity.

4. **Identify 3x3 Subgrids**:
    - Use `(row // 3, col // 3)` to track numbers in 3x3 subgrids.