### Anki Flash Card Based on Key Points

#### Front
What are the key steps to solve the "Product of Array Except Self" problem?

#### Back
1. **Two-pass approach**:
   - First pass computes the product of all elements to the left of each index.
   - Second pass computes the product of all elements to the right of each index using a `postfix` variable.

2. **Postfix product**:
   - In the second pass, use a `postfix` variable to track the running product of elements from right to left.

3. **Space Complexity**:
   - The solution uses `O(1)` extra space (excluding the result array) by updating the result array in place.

4. **Edge Cases**:
   - Handles arrays with zeroes or arrays with only one element efficiently without division.