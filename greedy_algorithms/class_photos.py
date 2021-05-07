# redshirt heights and blue shirt heights array will have the same length
# blue in the back row and red in front
# have to check whether we can take a photo
# have to check whether for every red shirt there is a blue shirt
# on the back with greater height

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.

    redShirtHeights.sort()
    blueShirtHeights.sort()

    index = 0
    index_2 = 0

    is_blue_bigger = True
    is_red_bigger = True

    while index < len(redShirtHeights) and index_2 < len(blueShirtHeights):
        print("blue ", blueShirtHeights[index_2])
        print("red ", redShirtHeights[index])
        is_blue_bigger = blueShirtHeights[index_2] > redShirtHeights[index] and is_blue_bigger
        is_red_bigger = blueShirtHeights[index_2] < redShirtHeights[index] and is_red_bigger
        index += 1
        index_2 += 1

    return is_blue_bigger or is_red_bigger


if __name__ == '__main__':
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    can_take = classPhotos(redShirtHeights, blueShirtHeights)
    print(can_take)
