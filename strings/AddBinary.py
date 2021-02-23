def addBinary(first_string: str, second_string: str):
    max_length = max(len(first_string), len(second_string))

    first_string = first_string.zfill(max_length)
    second_string = second_string.zfill(max_length)

    carry = 0
    sum = ''

    for i in range(max_length - 1, -1, -1):
        print("first " + first_string[i] + " second " + second_string[i])
        current_sum = carry

        if first_string[i] == '1':
            current_sum += 1
        else:
            current_sum += 0

        if second_string[i] == '1':
            current_sum += 1
        else:
            current_sum += 0

        if current_sum == 1:
            sum = "1" + sum
            carry =0
        elif current_sum == 2:
            sum = "0" + sum
            carry = 1
        elif current_sum == 3:
            sum = "1" + sum
            carry = 1
        else:
            sum = "0" + sum
            carry = 0

        print("carry "+str(carry))
        print("sum "+sum)
        if carry != 0 and i == 0:
            sum = "1"+sum

    return sum.zfill(max_length)


if __name__ == '__main__':
    print(addBinary("1010", "1011"))
