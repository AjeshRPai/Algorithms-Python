### Anki Card Based on Key Points

#### Front
What are the key steps to find the longest consecutive sequence in an unsorted array of numbers?

#### Back
1. **Convert the List to a Set**:
   - This allows for fast lookups (O(1) time) when checking for consecutive numbers.

2. **Identify Sequence Start**:
   - A number is the start of a sequence if `n - 1` is not present in the set.

3. **Count Sequence Length**:
   - Use a loop to count how long the consecutive sequence goes from the start.

4. **Track the Longest Sequence**:
   - Keep updating the `longest` variable when you find a sequence longer than the previous one