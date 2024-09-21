from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no permutation of s1 can be a substring of s2
        if len(s1) > len(s2):
            return False

        # Initialize frequency counts of both s1 and the first window in s2
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # Calculate initial matches between s1 and first window of s2
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # Start sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:  # If all characters match, return True
                return True

            # Add the new character to the window
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the old character from the window
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Simple permutation exists
    s1_1 = "ab"
    s2_1 = "eidbaooo"
    print(solution.checkInclusion(s1_1, s2_1))  # Expected: True

    # Test Case 2: No permutation
    s1_2 = "ab"
    s2_2 = "eidboaoo"
    print(solution.checkInclusion(s1_2, s2_2))  # Expected: False

    # Test Case 3: Larger strings, permutation exists
    s1_3 = "adc"
    s2_3 = "dcda"
    print(solution.checkInclusion(s1_3, s2_3))  # Expected: True

    # Test Case 4: Exact match of s1 and s2
    s1_4 = "a"
    s2_4 = "a"
    print(solution.checkInclusion(s1_4, s2_4))  # Expected: True

    # Test Case 5: No match at all
    s1_5 = "hello"
    s2_5 = "world"
    print(solution.checkInclusion(s1_5, s2_5))  # Expected: False
