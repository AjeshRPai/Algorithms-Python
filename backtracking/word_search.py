from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == word[0]:
                if dfs(board, word, 0, row, column, rows, columns):
                    return True

    return False


def dfs(board: List[List[str]], word: str, index: int, row: int, column: int, rows: int, columns: int):
    if row < 0 or row >= rows or column < 0 or column >= columns or board[row][column] != word[index]:
        return False
    if index == len(word) - 1:
        return True

    board[row][column] = '#'

    if (dfs(board, word, index + 1, row - 1, column, rows, columns)
            or dfs(board, word, index + 1, row + 1, column, rows, columns)
            or dfs(board, word, index + 1, row, column - 1, rows, columns)
            or dfs(board, word, index + 1, row, column + 1, rows, columns)):
        return True

    board[row][column] = word[index]
    return False


if __name__ == '__main__':
    boardValue = [["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]],
    word = "CAT"
    print(exist(boardValue, word))
