def numDecodings(s):
    if not s or s[0] == "0":
        return 0

    dp = [1, 1]
    for i in range(1, len(s)):
        ways = 0
        if s[i] != "0":
            ways += dp[-1]
        if 10 <= int(s[i-1:i+1]) <= 26:
            ways += dp[-2]
        dp.append(ways)
    return dp[-1]
