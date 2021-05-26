def reverse_word(string):
    stack = []
    reversed = ""
    for letter in string:
        if letter != " ":
            stack.append(letter)
        else:
            while len(stack) != 0:
                reversed = reversed + stack.pop()
            reversed += " "

    while len(stack) != 0:
        reversed = reversed + stack.pop()

    return reversed


# Let's jump off
def reverse_word2(string):
    start = 0
    for index in range(len(string)):
        if string[index] == " ":
            end = index
            swap_letters(string, start, end)
            start = end + 1

    return string

# this would not work since the in place
# swapping is not supported in python
def swap_letters(word, start, end):
    while start <= end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    word = "lets jump off"
    print(reverse_word2(word))
