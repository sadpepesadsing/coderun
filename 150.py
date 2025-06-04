import sys


def main():
    n = int(input())
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[n]
    
if __name__ == '__main__':
    print(main())
