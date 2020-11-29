arr = [5, 8, 7, 1, 9]


def lis(arr):
    n = len(arr)
    if n == 1:
        return arr
    dp = [1] * n
    i = 1
    while i < n:
        j = 0
        while j < i:
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] += 1
            j += 1
        i += 1
    print("LIS ", max(dp))
    i = dp.index(max(dp))
    count = dp[i]
    ans = [arr[i]]
    i -= 1
    while i >= 0:
        if dp[i] + 1 == count:
            ans.insert(0, arr[i])
            count -= 1
        i -= 1
    print(ans)


lis(arr)
