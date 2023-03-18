from collections import deque

x=int(input())
Q=deque([x])
dp=[0]*(x+1)

while Q:
    c=Q.popleft()
    if c==1: break

    Q.append(c-1)
    dp[c-1]=dp[c]+1
    if c%3==0 :
        Q.append(c//3)
        dp[c//3]=min(dp[c//3],dp[c]+1)
    if c%2==0 :
        Q.append(c//2)
        dp[c//2]=min(dp[c//2],dp[c]+1)


print(dp[1])

