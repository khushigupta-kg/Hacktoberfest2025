from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())
