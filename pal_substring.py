# Python program to find the longest palindromic substring in a given string.

def longest_palin(s):
	# Initialize variables to keep track 
	# of the longest palindrome and its length.
	count = -1
	ans = ""

	# Get the length of the input string.
	n = len(s)
	
	# Create a boolean 2D array to 
	# store palindrome information.
	dp = [[False] * n for _ in range(n)]

	# Iterate through different substring lengths.
	for g in range(n):
		for i in range(n - g):
			j = i + g
			# Check if the substring is of length 1 (base case).
			if g == 0:
				dp[i][j] = True
			# Check if the substring is of length 2 (base case).
			elif g == 1:
				dp[i][j] = (s[i] == s[j])
			else:
				# Check if the current substring is a 
				# palindrome based on its ends.
				dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

			# Update the longest palindrome and its length if found.
			if dp[i][j] and count < j - i + 1:
				ans = s[i:j + 1]
				count = len(ans)
	return ans

def find_longest_palindrome( s):
       longest = ''
       n = len(s)
       for i in range(n):
        for j in range(i+1,n+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word          
       return longest

# Input string
str = "forgeeksskeegfor"
# Print the longest palindromic substring.
print(longest_palin(str))
print (find_longest_palindrome(str))
