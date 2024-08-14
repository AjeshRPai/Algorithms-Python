from typing import List

from collections import defaultdict

def isValid(s: str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack


#Driver code
if __name__ == "__main__":
    s = "([{}])"
    k = isValid(s)
    print(k)
