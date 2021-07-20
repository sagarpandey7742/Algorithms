def fun(s):

    def solve(s, i, j, isTrue):

        if i>j:
            return False
        if i==j:
            if isTrue:
                if s[i]=="T":
                    return True
                else:
                    return False
            else:
                if s[i]=="F":
                    return True
                else:
                    return False

        ans=0

        for k in range(i+1, j, 2):
            lt=solve(s, i, k-1, True)
            lf=solve(s, i, k-1, False)
            rt=solve(s, k+1, j, True)
            rf=solve(s, k+1, j, False)

            if s[k]=="&":
                if isTrue:
                    ans+=lt*rt
                else:
                    ans+=lt*rf + lf*rf + lf*rt
            elif s[k]=="|":
                if isTrue:
                    ans+=lt*rf + lt*rt + lf*rt
                else:
                    ans+=lf*rf
            else:
                if isTrue:
                    ans+=lt*rf+ lf*rt
                else:
                    ans+=lt*rt + lf*rf
        return ans

    return solve(s, 0, len(s)-1, True)

print(fun("T|T&F^T"))