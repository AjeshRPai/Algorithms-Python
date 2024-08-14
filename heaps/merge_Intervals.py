from typing import List

# Link https://neetcode.io/problems/merge-intervals

def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]
        print(lastEnd)

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

if __name__ == '__main__':
    print(merge(intervals=[[1, 3], [1, 5], [6, 7]]))
    expectedOutput = [[1, 5], [6, 7]]
