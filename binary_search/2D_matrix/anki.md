### Anki Card Based on Key Points

#### Front
How do you search for a target in a 2D matrix where each row is sorted?

#### Back
1. **Binary Search to Find the Row**:
   - Use binary search to identify the row where the target might exist. Compare the target with the first and last elements of each row.

2. **Binary Search Within the Row**:
   - After narrowing down the row, apply binary search to search for the target within that row.

3. **Handle Edge Cases**:
   - Consider edge cases like a single row/column or target values smaller/larger than row boundaries.