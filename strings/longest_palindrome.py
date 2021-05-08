def is_palindrome(input_string):
    if len(input_string) == 0:
        return True

    length = len(input_string)

    # Finding middle index of string
    middle = length // 2

    start = 0
    end = len(input_string) - 1
    while start <= middle <= end:
        if input_string[start] == input_string[end]:
            start += 1
            end -= 1
        else:
            return False

    return True


def longestPalindromicSubstring(string):
    longest = ''
    for index in range(0, len(string)):
        for index_2 in range(index, len(string)):
            substring = string[index:index_2 + 1]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest


if __name__ == '__main__':
    # run algorithm
    string = "abaxyzzyxf"
    palindrome = longestPalindromicSubstring(string)
    print(palindrome)
