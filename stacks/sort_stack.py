def insertInStack(stack, element):
    if len(stack) == 0 or stack[len(stack)-1]<element:
        stack.append(element)
        return

    current_top = stack.pop()
    insertInStack(stack, element)
    stack.append(current_top)


def sortStack(stack):
    if len(stack) < 2:
        return stack
    top = stack.pop()
    sortStack(stack)
    insertInStack(stack, top)
    return stack


if __name__ == '__main__':
    stack = [-5, 2, -2, 4, 3, 1]
    print(sortStack(stack))
