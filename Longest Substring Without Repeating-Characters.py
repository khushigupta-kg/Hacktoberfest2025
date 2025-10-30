def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    res = 0

    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1
        seen[ch] = r
        res = max(res, r - l + 1)
    return res
