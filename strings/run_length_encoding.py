def runLengthEncoding(string):
    output_string = ""
    last_character_count = 1

    for index in range(1, len(string)):
        current_char = string[index]
        previous_char = string[index - 1]

        if current_char == previous_char and last_character_count < 9:
            last_character_count += 1
        else:
            output_string += str(last_character_count)
            output_string += previous_char
            last_character_count = 1

    output_string += str(last_character_count)
    output_string += string[len(string) - 1]

    return output_string


if __name__ == '__main__':
    input_string = "AABBCCDDDD"
    input_string2= "AAAAAAAAAAAAABBCCCCDD"
    print(runLengthEncoding(input_string))
    print(runLengthEncoding(input_string2))
