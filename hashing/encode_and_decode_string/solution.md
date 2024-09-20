###  Key Points to Memorize this Solution

1. **Encoding Process:**
    - Each string is encoded by storing its length, followed by a `#` separator, and then the string itself. This allows
      for a clear boundary between different strings during decoding.

2. **Decoding Process:**
    - When decoding, we first identify the length of each string by reading the characters before the `#` symbol. After
      getting the length, we extract the string of that length and continue this process for the entire encoded string.

3. **Special Characters and Edge Cases:**
    - The use of `#` as a delimiter avoids ambiguity when encoding strings with special characters like `#` or empty
      strings. The length stored before each string ensures no confusion.

4. **Time Complexity:**
    - Both encoding and decoding are linear operations, `O(n)`, where `n` is the total length of all strings combined.

