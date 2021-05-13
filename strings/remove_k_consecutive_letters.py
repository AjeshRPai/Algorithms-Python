from queue import LifoQueue

# https://www.geeksforgeeks.org/reduce-the-string-by-removing-k-consecutive-identical-characters/

def remove_kth_consecutive(word, k):
    stack = LifoQueue(len(word))

    frequency = 1
    for letter in word:

        if stack.empty():
            stack.put((letter, frequency))
        else:
            letter_at_top, frequency_of_letter = stack.get()
            if letter_at_top == letter:
                frequency_of_letter += 1
                if frequency_of_letter<k:
                    stack.put((letter, frequency_of_letter))
            else:
                stack.put((letter_at_top, frequency_of_letter))
                stack.put((letter, frequency))

    end_word = ''

    while not stack.empty():
        letter, frequency = stack.get()
        if frequency <= k:
            end_word = letter+end_word

    return end_word

if __name__ == '__main__':
    word = "qddxxxd"
    end_word = remove_kth_consecutive(word,3)
    print(end_word)
