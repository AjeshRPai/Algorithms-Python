# You are given a
def print2dArray(T):
    for r in T:
        for c in r:
            print(c, end=" ")
        print()


def getKnapsackItems(cell, items):
    sequence = []
    row = len(cell) - 1
    column = len(cell[0]) - 1

    while row > 0:
        if cell[row][column] == cell[row - 1][column]:
            row -= 1
        else:
            sequence.append(row - 1)
            print("added",row-1)
            print("column",column)
            print("to remove",items[row - 1][1])
            column -= items[row - 1][1]
            row -= 1
        if column == 0:
            break
    return list(reversed(sequence))


def knapsackProblem(items, capacity):
    values = []
    item_weight = []

    print("capacity", capacity)

    for item in items:
        values.append(item[0])
        item_weight.append(item[1])

    cell = [[0 for x in range(capacity + 1)] for y in range(0, len(values) + 1)]


    for row in range(1, len(values) + 1):
        current_weight = item_weight[row - 1]
        current_value = values[row - 1]

        for column in range(0, capacity + 1):
            if current_weight > column:
                cell[row][column] = cell[row - 1][column]
            else:
                previous_value = cell[row - 1][column]

                space_left = column - current_weight

                value_of_space_left = cell[row - 1][space_left]
                cell[row][column] = max(previous_value,
                                        (current_value + value_of_space_left))


    return [cell[-1][-1],getKnapsackItems(cell,items)]


if __name__ == '__main__':
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    items_to_take = knapsackProblem(items, capacity)
    print(items_to_take)
