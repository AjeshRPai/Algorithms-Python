from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # determine which word should be on one line
        # get the line_words with start index
        #
        # format the line
        def get_line_words(current_index):
            cur_word_in_line = []
            cur_length = 0

            while current_index < len(words) and cur_length + len(words[current_index]) <= maxWidth:
                cur_word_in_line.append(words[current_index])
                cur_length += len(words[current_index]) + 1
                current_index += 1
            return cur_word_in_line

        # the cur_line is a list of words in a line
        def format_line(cur_line_of_words, index):
            if not cur_line_of_words:
                return

            print("line of words", cur_line_of_words)
            # should be distributed evenly
            # empty spaces on left if not evenly
            # first and last line should be
            base_length = -1
            for word in cur_line_of_words:
                base_length += len(word) + 1

            extra_spaces = maxWidth - base_length

            if len(cur_line_of_words) == 1 or index == len(words):
                return " ".join(cur_line_of_words) + " " * extra_spaces

            word_count = len(cur_line_of_words) - 1
            space_per_word = extra_spaces // word_count
            extra_spaces_at_end = extra_spaces % word_count

            for i in range(extra_spaces_at_end):
                cur_line_of_words[i] += " "

            # we are adding space to every word
            for j in range(word_count):
                cur_line_of_words[j] += " " * space_per_word

            return " ".join(cur_line_of_words)

        result = []
        index = 0

        while index < len(words):
            cur_line = get_line_words(index)  # Get words for the current line
            index += len(cur_line)  # Move to the next set of words
            result.append(format_line(cur_line, index))  # Format and store the line

        return result

def test_fullJustify():
    sol = Solution()

    # Test Case 1
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    print(sol.fullJustify(words1, maxWidth1))

    # Test Case 2 (Single Word Per Line)
    words2 = ["Hello", "world"]
    maxWidth2 = 5
    print(sol.fullJustify(words2, maxWidth2))

    # # Test Case 3 (Single Word Longer than maxWidth)
    # words3 = ["Supercalifragilisticexpialidocious"]
    # maxWidth3 = 10
    # print(sol.fullJustify(words3, maxWidth3))
    #
    # # Test Case 4 (Empty List)
    # words4 = []
    # maxWidth4 = 10
    # print(sol.fullJustify(words4, maxWidth4))

    # Test Case 5 (Last Line Left-Aligned)
    words5 = ["A", "lot", "of", "words", "to", "justify"]
    maxWidth5 = 14
    print(sol.fullJustify(words5, maxWidth5))

if __name__ == '__main__':
    test_fullJustify()
