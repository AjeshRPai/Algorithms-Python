from typing import List

class Solution:

    # Encode list of strings into a single string
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # Each string is encoded as its length + '#' + the string itself
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    # Decode the encoded string back into a list of strings
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        # Process the encoded string character by character
        while i < len(s):
            # Find the position of the next '#' to determine the length of the next string
            j = i
            while s[j] != '#':
                j += 1

            # Extract the length of the string
            length_of_string = int(s[i:j])

            # Move the pointer to the start of the actual string
            i = j + 1

            # Extract the string using the length
            actual_string = s[i:i + length_of_string]
            decoded_list.append(actual_string)

            # Move the pointer to the next encoded string
            i = i + length_of_string

        return decoded_list


if __name__ == "__main__":
    solution = Solution()

    # Scenario 1: General case with normal strings
    strs1 = ["hello", "world", "test"]
    encoded1 = solution.encode(strs1)
    decoded1 = solution.decode(encoded1)
    print(f"Scenario 1 - Encoded: {encoded1}, Decoded: {decoded1}")

    # Scenario 2: Case with empty strings
    strs2 = ["", "abc", "", "def"]
    encoded2 = solution.encode(strs2)
    decoded2 = solution.decode(encoded2)
    print(f"Scenario 2 - Encoded: {encoded2}, Decoded: {decoded2}")

    # Scenario 3: Case with special characters
    strs3 = ["#", "##", "abc#def", ""]
    encoded3 = solution.encode(strs3)
    decoded3 = solution.decode(encoded3)
    print(f"Scenario 3 - Encoded: {encoded3}, Decoded: {decoded3}")

    # Scenario 4: All strings are empty
    strs4 = ["", "", ""]
    encoded4 = solution.encode(strs4)
    decoded4 = solution.decode(encoded4)
    print(f"Scenario 4 - Encoded: {encoded4}, Decoded: {decoded4}")

    # Scenario 5: Large string
    strs5 = ["a" * 1000, "b" * 500, "c" * 100]
    encoded5 = solution.encode(strs5)
    decoded5 = solution.decode(encoded5)
    print(f"Scenario 5 - Encoded: {encoded5}, Decoded: {decoded5}")
