## Anki card:

**Front**:
Describe the TimeMap data structure and its key operations (set and get).

**Back**:
TimeMap is a data structure that stores key-value pairs with timestamps.
- Internal structure: Dictionary mapping keys to lists of (timestamp, value) tuples.
- set(key, value, timestamp): Appends (timestamp, value) to the list for the given key.
- get(key, timestamp): Uses binary search to find the most recent value for the key at or before the given timestamp.
- Time complexity: O(1) for set, O(log n) for get (where n is the number of values for a key).
- Handles edge cases: Non-existent keys, timestamps before any set operation.
