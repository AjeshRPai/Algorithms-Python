class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, return empty string
        if not t:
            return ""

        # Count characters in t
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Initialize sliding window
        window = {}
        chars_matched = 0
        chars_needed = len(char_count_t)

        # Initialize result
        min_window = ""
        min_length = float('inf')

        left = 0
        # Expand window to the right
        for right in range(len(s)):
            # Add right character to window
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Check if we've matched a character from t
            if char in char_count_t and window[char] == char_count_t[char]:
                chars_matched += 1

            # Try to contract window from the left
            while chars_matched == chars_needed:
                # Update result if current window is smaller
                if right - left + 1 < min_length:
                    min_window = s[left:right + 1]
                    min_length = right - left + 1

                # Remove left character from window
                window[s[left]] -= 1
                if s[left] in char_count_t and window[s[left]] < char_count_t[s[left]]:
                    chars_matched -= 1

                left += 1

        return min_window

if __name__ == '__main__':
    solution = Solution()

    # Test case 1: Normal case
    s1, t1 = "ADOBECODEBANC", "ABC"
    print(f"Test 1: s = {s1}, t = {t1}")
    print(f"Result: {solution.minWindow(s1, t1)}")
    print(f"Expected: BANC\n")

    # Test case 2: Substring at the beginning
    s2, t2 = "ABCDEFG", "AC"
    print(f"Test 2: s = {s2}, t = {t2}")
    print(f"Result: {solution.minWindow(s2, t2)}")
    print(f"Expected: ABC\n")

    # Test case 3: Substring at the end
    s3, t3 = "ABCDEFG", "FG"
    print(f"Test 3: s = {s3}, t = {t3}")
    print(f"Result: {solution.minWindow(s3, t3)}")
    print(f"Expected: FG\n")

    # Test case 4: No valid substring
    s4, t4 = "ABCDEFG", "Z"
    print(f"Test 4: s = {s4}, t = {t4}")
    print(f"Result: {solution.minWindow(s4, t4)}")
    print(f"Expected: \n")

    # Test case 5: t is empty
    s5, t5 = "ABCDEFG", ""
    print(f"Test 5: s = {s5}, t = {t5}")
    print(f"Result: {solution.minWindow(s5, t5)}")
    print(f"Expected: \n")
