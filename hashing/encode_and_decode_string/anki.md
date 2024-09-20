### 4. Anki Flash Card Based on Key Points

#### Front

What are the key steps involved in encoding and decoding a list of strings using a custom format?

#### Back

1. **Encoding:**
    - Each string is encoded as `length_of_string + '#' + string`. This format ensures we can differentiate between
      consecutive strings, even if they contain special characters or are empty.

2. **Decoding:**
    - While decoding, we first extract the length of each string from the characters before the `#` symbol, then extract
      the string based on that length, and repeat the process.

3. **Handling Special Characters:**
    - The `#` separator effectively handles special characters like `#` within the strings or empty strings.

4. **Efficiency:**
    - Both encoding and decoding are performed in `O(n)` time, where `n` is the total length of all strings combined.