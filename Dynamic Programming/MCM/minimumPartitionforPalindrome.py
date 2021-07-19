s="nitinaab"
n=len(s)
dp=[[-1 for j in range(n)] for i in range(n)]

def fun(s, i, j, ans):
    if dp[i][j]!=-1:
        return dp[i][j]
    if i>j:
        dp[i][j]=0
        return 0
    if s[i:j+1]==s[i:j+1][::-1]:
        dp[i][j] = 0
        return 0
    for k in range(i,j):
        temp=1+ fun(s, i, k, ans)+ fun(s, k+1, j,ans)
        ans=min(ans, temp)
    dp[i][j] = ans
    return ans
ans=fun(s, 0, len(s)-1, 10**10)

for d in dp:
    print(*d, sep='\t')

print(ans)