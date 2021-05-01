# given two strings
# calculate the number of operations
# to be performed to make them equal

# supported operations are insertion,deletion,removal

# its a dynamic programming question where u use
# dynamic programming to solve the question


def levenshteinDistance(str1, str2):
    rows = len(str1) + 1
    columns = len(str2) + 1

    cell = [[x for x in range(columns)] for y in range(rows)]
    # base case has to be [0,1,2,3,4]

    print(cell)

    for row in range(1,rows):
        cell[row][0] = cell[row-1][0]+1

    print(cell)

    for row in range(1,rows):
        for column in range(1,columns):
            if str1[row-1] == str2[column-1]:
                cell[row][column] = cell[row - 1][column - 1]
            else:
                cell[row][column] = 1 + min(cell[row][column - 1], cell[row - 1][column], cell[row - 1][column - 1])

    print(cell)

    return cell[-1][-1]


if __name__ == '__main__':
    str1 = "yabd"
    str2 = "abc"
    no_of_steps = levenshteinDistance(str1, str2)
    print(no_of_steps)
