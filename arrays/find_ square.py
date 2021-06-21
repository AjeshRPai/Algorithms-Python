import unittest

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIndex = 0
    largerValueIndex = len(array)-1

    for index in reversed(range(len(array))):
        smallerValue = array[smallerValueIndex]
        largerValue = array[largerValueIndex]

        if abs(smallerValue)>abs(largerValue):
            sortedSquares[index] = smallerValue*smallerValue
            smallerValueIndex+=1
        else:
            sortedSquares[index] = largerValue*largerValue
            largerValueIndex-=1

    return sortedSquares

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    output = sortedSquaredArray(array)
    print(output)

    array2 = [-3,-2,-1]
    output = sortedSquaredArray(array2)
    print(output)

