def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


if __name__ == '__main__':
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    grouped = groupAnagrams(words)
    print(grouped)
