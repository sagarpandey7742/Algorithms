def fun(s, i, j, ans):
    if i>=j:
        return 0
    if s[i:j+1]==s[i:j+1][::-1]:
        return 0
    for k in range(i,j):
        temp=1+ fun(s, i, k, ans)+ fun(s, k+1, j,ans)
        ans=min(ans, temp)
    return ans
s="nitinaab"
print(fun(s, 0, len(s)-1, 10**10))
