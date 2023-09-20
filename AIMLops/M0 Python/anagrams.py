from collections import defaultdict


def are_anagrams(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())


def group_anagrams(words: list) -> list:
    anagrams_dict = defaultdict(list)
    for word in words:
        dict_key = "".join(sorted(word))
        # if dict_key in anagrams_dict.keys():
        anagrams_dict[dict_key].append(word)
        # else:
        #     anagrams_dict[dict_key] = [word]
    # print(anagrams_dict)
    return [anags for anags in anagrams_dict.values() if len(anags) > 1]


words = [line.strip() for line in open("words.txt")]
print(words)
print(group_anagrams(words))

# print(are_anagrams("pera","sam"))
# print(are_anagrams("sam","mas"))
