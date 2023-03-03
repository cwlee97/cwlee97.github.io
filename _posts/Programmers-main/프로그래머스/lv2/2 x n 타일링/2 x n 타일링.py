import sys
sys.setrecursionlimit(60000)

def dynamic(n, dp):
  if n in dp:
    return dp[n]
  else:
    dp[n] = (dynamic(n-1, dp) + dynamic(n-2, dp)) % 1000000007
    return dp[n]

def solution(n):
    dp = {-1: 0, 0: 1, 1: 1, 2: 2, 3: 3}
    dynamic(n, dp)
    answer = dp[n]
    return answer