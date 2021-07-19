def printScs(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    maxlengthLCS = dp[m][n]

    scsLength = m + n - maxlengthLCS

    print("SCS length =", scsLength)

    i = m
    j = n
    ans = ""

    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            ans += s[i - 1]
            i -= 1
            j -= 1
        elif dp[i][j - 1] > dp[i - 1][j]:
            ans += t[j - 1]
            j -= 1
        else:
            ans += s[i - 1]
            i -= 1
    while i > 0:
        ans += s[i - 1]
        i -= 1
    while j > 0:
        ans += t[j - 1]
        j -= 1
    return ans[::-1]


print(printScs("AGGTAB", "GXTXAYB"))
