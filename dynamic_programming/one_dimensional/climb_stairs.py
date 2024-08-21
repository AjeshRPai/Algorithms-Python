def climbStairs(n: int) -> int:
    if (n <= 3):
        return n

    ways = [0] * (n+1)

    ways[0] = 0
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        print(i)
        ways[i] = ways[i - 1] + ways[i - 2]
        print(ways)

    return ways[n]

if __name__ == '__main__':
    output = climbStairs(5)
    print(output)