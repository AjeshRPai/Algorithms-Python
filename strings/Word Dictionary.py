def wordBreak(dict, str):
    if not str:
        return

    output_array = []

    for i in range(0, len(str)):
        first_letter = str[i]

        if first_letter in dict:
            output_array.append(first_letter)

        rest_of_the_letters = str[i + 1:]
        for j in range(1, len(rest_of_the_letters) + 1):
            rest_of_letter = rest_of_the_letters[:j]
            possible_match = first_letter + rest_of_letter
            print(possible_match)
            if possible_match in dict:
                output_array.append(possible_match)
    return output_array


# Word Break Problem Implementation in Python
if __name__ == '__main__':
    # List of strings to represent a dictionary
    dict = [
        'quick', 'brown', 'the', 'fox'
    ]

    # input string
    str = "thequickbrownfox"

    word_break = wordBreak(dict, str)
    print(word_break)
