N = int(input())
dp = [0]*(N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i%2==0: dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0: dp[i] = min(dp[i], dp[i//3]+1)

count = dp[N]
print(N, end= ' ')
for i in range(N-1,0,-1):
    if dp[i]<count:
        count=dp[i]
        print(i, end=' ')

