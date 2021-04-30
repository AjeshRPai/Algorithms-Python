
def longestCommonSubsequence(str1, str2):
    rows = len(str1) + 1
    columns = len(str2) + 1
    cell = [[[] for i in range(columns)] for j in range(rows)]
    for i in range(1, rows):
        for j in range(1, columns):
            if str1[i - 1] == str2[j - 1]:
                cell[i][j] = cell[i - 1][j - 1] + [str1[i-1]]
            else:
                cell[i][j] = max(cell[i - 1][j], cell[i][j - 1], key=len)
    return cell[-1][-1]


if __name__ == '__main__':
    str1 = "ZXVVYZW"
    str2 = "XKYKZPW"
    lcs = longestCommonSubsequence(str1, str2)
    print(lcs)
