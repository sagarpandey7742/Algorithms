arr=[1, 2, 3, 4, 3]
n=len(arr)
dp=[[-1 for j in range(n)] for i in range(n)]

def mcm(arr, i, j, ans):
    if dp[i][j]!=-1:
        return dp[i][j]
    if i>=j:
        dp[i][j]=0
        return 0
    for k in range(i, j):
        temp= mcm(arr, i, k, ans) + mcm(arr, k+1, j, ans)+ arr[i-1]*arr[k]*arr[j]
        ans=min(ans, temp)
    dp[i][j]=ans
    return dp[i][j]


ans=10**10
print(mcm(arr, 1, n-1, ans))

for d in dp:
    print(*d, sep='\t')


