s="nitinaab"
n = len(s)
dp = [[-1 for j in range(n)] for i in range(n)]
p = [[-1 for i in range(n)] for j in range(n)]


def pal(s, i, j):
    ii = i
    jj = j
    if p[i][j] != -1:
        return p[i][j]
    flag = 0
    while i <= j:
        if s[i] != s[j]:
            flag = 1
            break
        i += 1
        j -= 1
    if flag == 0:
        p[ii][jj] = 1
    else:
        p[ii][jj] = 0
    return p[ii][jj]


def fun(s, i, j, ans):
    if dp[i][j] != -1:
        return dp[i][j]
    if i > j:
        dp[i][j] = 0
        return 0
    if pal(s, i, j):
        dp[i][j] = 0
        return 0
    for k in range(i, j):
        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = fun(s, i, k, ans)
        if dp[k + 1][j] != -1:
            right = dp[k + 1][j]
        else:
            right = fun(s, k + 1, j, ans)

        temp = 1 + left + right
        ans = min(ans, temp)
    dp[i][j] = ans
    return ans


ans = fun(s, 0, len(s) - 1, 10 ** 10)

for d in dp:
    print(*d, sep='\t')

print()
for pp in p:
    print(pp)

print(ans)