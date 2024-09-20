###  Key Points to Memorize this Solution

1. **Use a Set for Fast Lookup**:
   - Convert the list to a set so you can check for the presence of numbers in O(1) time.

2. **Identify the Start of a Sequence**:
   - A number is the start of a sequence if `n - 1` is not in the set.

3. **Count Consecutive Numbers**:
   - For each sequence starting number, count how long the consecutive sequence goes.

4. **Track the Longest Sequence**:
   - Keep track of the longest sequence found using a variable `longest`, updating it as you find longer sequences.

