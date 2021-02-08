def findThreeLargestNumbers(array):
    # Write your code here
    max = [None, None, None]
    for i in array:
        if max[2] is None or i >= max[2]:
            max[0] = max[1]
            max[1] = max[2]
            max[2] = i
        elif max[1] is None or i >= max[1]:
            max[0] = max[1]
            max[1] = i
        elif max[0] is None or i >= max[0]:
            max[0] = i
    return max

if __name__ == '__main__':
    print(findThreeLargestNumbers([2, 3, 4, 6, 7, 8]))
