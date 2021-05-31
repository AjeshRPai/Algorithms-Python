def sortStack(stack):
    if len(stack) < 2:
        return stack

    current_value = stack.pop()
    sortStack(stack)

    insert_recursive(stack, current_value)
    return stack


def insert_recursive(current_stack, current_value):
    if len(current_stack) == 0 or current_value >= current_stack[len(current_stack) - 1]:
        current_stack.append(current_value)
        return

    top_element = current_stack.pop()
    insert_recursive(current_stack, current_value)
    current_stack.append(top_element)


if __name__ == '__main__':
    stack = [-5, 2, -2, 4, 3, 1]
    print(sortStack(stack))
