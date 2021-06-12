def generateDocument(characters, document):
    character_map = {}
    for character in characters:
        if character not in character_map:
            character_map[character] = 1
        else:
            character_map[character] += 1

    for character in document:
        if character in character_map and character_map[character] > 0:
            character_map[character] -= 1
        else:
            return False

    return True

if __name__ == '__main__':
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    print(generateDocument(characters, document))
