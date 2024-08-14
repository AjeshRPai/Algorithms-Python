from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(intervals)):
        print(intervals[i])
        # compare the second value of the new interval and first value of interval
        # if second value is less, that means the new interval is before the taken interval
        # so we add the interval to the beginning
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            print("adding interval before and then interval", res + intervals[i:])
            return res + intervals[i:]
        # compare the first value of new interval with last value of interval [1,2] [3,4] => [1,2] [3,4]
        # since the starting of new interval is more, we add it to the end
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            print("adding to res", res)
        else:
            print("case of overlapping", "get the min and max of outer")
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
    res.append(newInterval)
    return res


if __name__ == '__main__':
    print(insert(intervals=[[1, 2], [3, 5], [9, 10]], newInterval=[6, 7]))
    expectedOutput = [[1, 6]]
