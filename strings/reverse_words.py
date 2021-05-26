def reverseWordsInString(string):
    words = []
    start = 0

    # store in the list untill space occurs
    # then reverse the list
    for index in range(len(string)):
        character = string[index]

        if character == " ":
            print(string[start:index])
            words.append(string[start:index])
            start = index
        elif string[start] == " ":
            words.append(" ")
            start = index
    words.append(string[start:])
    reverseList(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start],
        start += 1
        end -= 1


if __name__ == '__main__':
    word = "Algoexpert is the best"
    print(reverseWordsInString(word))
