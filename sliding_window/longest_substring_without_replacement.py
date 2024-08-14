class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countOfLetters = {}
        left = 0
        maxOperations = 0

        for right in range(len(s)):
            countOfLetters[s[right]] = 1 + countOfLetters.get(s[right], 0)
            maxOperations = max(maxOperations, countOfLetters[s[right]])

            window = right - left + 1 # adding one since its index
            if window-maxOperations > k:
                countOfLetters[s[left]] -= 1
                left +=1
        return right - left + 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement(s="XYYX", k=2))
