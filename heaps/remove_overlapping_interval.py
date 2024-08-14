from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    res = 0
    prevEnd = intervals[0], [1]

    # iterate through the start value and end value of each interval
    for start, end in intervals[1:]:
        # if the start of this interval is after the end of the before one,
        # then there is no overlapping so just increment the prev end
        if start >= prevEnd:
            prevEnd = end
        else:
            # if there is an overlap, then add the operation to be done +1
            # get the min of the end value so that we can determine which is
            # the better interval to remove and update the end pointer
            res += 1
            prevEnd = min(end, prevEnd)
    return res


if __name__ == '__main__':
    print(eraseOverlapIntervals(intervals=[[1, 2], [3, 5], [9, 10]]))
    expectedOutput = [[1, 6]]
