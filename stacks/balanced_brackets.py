# function should return whether the word is
# balanced with regard to the brackets

# A String is balanced if it has same number
# of closing and opening brackets

# Closing bracket cant match a
# corresponding opening bracket if it comes before it

# Constraints,
# 1.The brackets are ([{
# 2.Ignore the other strings
# 3.The brackets cant overlap like [(])


def balancedBrackets(string):
    opening_brackets = "([{"
    closingBrackets = ")]}"
    stack = []
    start = 0
    end = len(string) - 1
    while start <= end:
        if string[start] in opening_brackets:
            stack.append(string[start])
        elif string[start] in closingBrackets:
            if len(stack) == 0:
                return False
            closing_bracket_index = closingBrackets.index(string[start])
            opening_bracket_index = opening_brackets.index(stack.pop())
            if opening_bracket_index != closing_bracket_index:
                return False
        start += 1

    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # test case 1
    word = "{([])}"
    # test case 2
    # if the word ends with a opening bracket
    word2 = "()()[]{"
    # test case 3
    # what if the closing bracket starts first
    # nothing will exist in stack
    word3 = ")[]}"
    print(balancedBrackets(word))
    print(balancedBrackets(word2))
    print(balancedBrackets(word3))
