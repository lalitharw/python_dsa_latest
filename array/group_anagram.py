from collections import defaultdict

def groupAnagram(arr):
    anagram = defaultdict(list)
    # solve using hashmap
    for adx in arr:

        # sort() -> is used with list
        # while sorted() -> is used with string,set,tuple and return new list
        key = "".join(sorted(adx))

        anagram[key].append(adx)
    return list(anagram.values())


print(groupAnagram( ["bat", "tab", "eat", "tea", "tan", "nat"]))