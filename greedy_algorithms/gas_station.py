from typing import List


def canCompleteCircuit( gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            res = i + 1

    return res


if __name__ == '__main__':
    print(canCompleteCircuit(gas = [1,2,3,4], cost = [2,2,4,1]))
