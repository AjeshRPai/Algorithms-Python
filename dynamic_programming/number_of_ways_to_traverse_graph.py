def numberOfWaysToTraverseGraph(width, height):
    xDistanceToCover = width - 1
    yDistanceToCover = height -1

    numerator = factorial(xDistanceToCover+yDistanceToCover)
    denominator = factorial(xDistanceToCover)* factorial(yDistanceToCover)

    return numerator/denominator

def factorial(num):
    result = 1
    for n in range(2,num+1):
        result *= n
    return result