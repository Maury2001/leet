def isMatch(s, p):
    # Create a 2D array filled with False
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns with '*' at the beginning
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            # If characters match or pattern has a '.'
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            # If pattern has '*'
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    # Result
    return dp[len(s)][len(p)]


# Example usage:
s = "ab"
p = ".*"
result = isMatch(s, p)
print(result)  # Output: True
