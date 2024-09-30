from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the end word is not in the word list, no transformation sequence exists
        if endWord not in wordList:
            return 0

        # Create a defaultdict to store pattern-to-word mappings
        nei = defaultdict(list)

        # Add the begin word to the word list
        wordList.append(beginWord)

        # Generate patterns for each word and map them to the original words
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # Initialize visited set, queue for BFS, and result counter
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        # Perform BFS
        while q:
            # Process all words at the current level
            for _ in range(len(q)):
                word = q.popleft()

                # If we've reached the end word, return the transformation sequence length
                if word == endWord:
                    return res

                # Generate patterns for the current word and explore neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        # If the neighbor hasn't been visited, add it to the queue
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            # Increment the transformation sequence length
            res += 1

        # If we can't reach the end word, return 0
        return 0


# Driver code with multiple scenarios
def test_word_ladder():
    solution = Solution()

    # Test case 1: Standard case
    begin_word1 = "hit"
    end_word1 = "cog"
    word_list1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(f"Test case 1: {solution.ladderLength(begin_word1, end_word1, word_list1)}")  # Expected output: 5

    # Test case 2: No transformation sequence exists
    begin_word2 = "hit"
    end_word2 = "cog"
    word_list2 = ["hot", "dot", "dog", "lot", "log"]
    print(f"Test case 2: {solution.ladderLength(begin_word2, end_word2, word_list2)}")  # Expected output: 0

    # Test case 3: Begin word is the end word
    begin_word3 = "hit"
    end_word3 = "hit"
    word_list3 = ["hot", "dot", "dog", "lot", "log"]
    print(f"Test case 3: {solution.ladderLength(begin_word3, end_word3, word_list3)}")  # Expected output: 1

    # Test case 4: Longer word sequence
    begin_word4 = "sail"
    end_word4 = "boat"
    word_list4 = ["sail", "bail", "bait", "bait", "boat"]
    print(f"Test case 4: {solution.ladderLength(begin_word4, end_word4, word_list4)}")  # Expected output: 5


if __name__ == '__main__':
    test_word_ladder()
    # Run the test cases
